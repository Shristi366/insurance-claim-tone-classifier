# P&C Insurance Claim Tone Classifier

Month 2 Assignment — classifies insurance claim descriptions using Google Gemini AI with Groq fallback.

---

## What it does

Reads 10 fictional P&C insurance claims from a CSV file and classifies each one across three dimensions:

* `claim_type` — motor | property | liability
* `tone` — calm | frustrated | urgent
* `legal_action_mentioned` — yes | no

---

## Project Structure

* `llm.py` — shared LLM helper (Gemini primary, Groq fallback)
* `classifier.py` — main classification script
* `claims.csv` — 10 fictional claim descriptions (input)
* `classified_claims.json` — classification results (output)

---

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API keys

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here
```

### 4. Run

```bash
python classifier.py
```

---

## Models Used

* Primary: `gemini/gemini-2.5-flash` (Google Gemini free tier)
* Fallback: `groq/llama-3.3-70b-versatile` (Groq free tier)
