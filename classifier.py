import csv
import json
import re
from llm import ask


claims = []
with open("claims.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        claims.append(row)

results = []

# --------------------------------------------------
# PROCESS EACH CLAIM
# --------------------------------------------------
for row in claims:
    claim_id    = row["claim_id"]
    description = row["description"]

    # --------------------------------------------------
    # AMBIGUOUS CLAIM NOTE — CLM010
    # CLM010 describes a cracked windshield caused by a
    # neighbour's child kicking a football. This is ambiguous
    # because the damage is to a vehicle (suggests motor) but
    # the cause is a third party's action (suggests liability).
    # The model classified it as "motor" because the physical
    # damage to the vehicle dominates the description.
    # Tone was "calm" — claimant says "I'm not angry" and
    # uses measured language throughout.
    # --------------------------------------------------

    prompt = f"""
You are an insurance claim classifier.
Analyze the insurance claim description below.

Classify:
1. claim_type
2. tone
3. legal_action_mentioned

Rules:
claim_type must be one of:
- motor
- property
- liability

tone must be one of:
- calm
- frustrated
- urgent

legal_action_mentioned must be:
- yes
- no

Return ONLY valid JSON like this:
{{
    "claim_type": "",
    "tone": "",
    "legal_action_mentioned": ""
}}

Claim Description:
"{description}"
"""

    try:
        response = ask([
            {"role": "system", "content": "You are a P&C insurance claim classifier."},
            {"role": "user",   "content": prompt}
        ])

        # Extract response text
        output_text = response.choices[0].message.content.strip()

        # Show which model actually answered
        # print(f"Provider used: {response.model}")

        # Extract JSON using regex
        json_match = re.search(r'\{.*\}', output_text, re.DOTALL)

        if json_match:
            classification = json.loads(json_match.group())

            result = {
                "claim_id"               : claim_id,
                "description"            : description,
                "claim_type"             : classification["claim_type"],
                "tone"                   : classification["tone"],
                "legal_action_mentioned" : classification["legal_action_mentioned"]
            }

            results.append(result)
            print(f"OK {claim_id} -> type={classification['claim_type']} | tone={classification['tone']} | legal={classification['legal_action_mentioned']}")

        else:
            print(f"Could not parse JSON for claim {claim_id}")

    except Exception as e:
        print(f"Error processing claim {claim_id}: {e}")

# --------------------------------------------------
# SAVE RESULTS TO JSON FILE
# --------------------------------------------------
with open("classified_claims.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("")
print("Classification completed successfully!")
print(f"Total claims processed: {len(results)}")
print("Results saved to classified_claims.json")