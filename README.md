\# P\&C Insurance Claim Tone Classifier



Month 2 Assignment — classifies insurance claim descriptions using Google Gemini AI with Groq fallback.



\## What it does

Reads 10 fictional P\&C insurance claims from a CSV file and classifies each one across three dimensions:

\- claim\_type — motor | property | liability

\- tone — calm | frustrated | urgent

\- legal\_action\_mentioned — yes | no



\## Project Structure

\- llm.py — shared LLM helper (Gemini primary, Groq fallback)

\- classifier.py — main classification script

\- claims.csv — 10 fictional claim descriptions (input)

\- classified\_claims.json — classification results (output)



\## Setup



\### 1. Create virtual environment

python -m venv venv

venv\\Scripts\\activate



\### 2. Install dependencies

pip install -r requirements.txt



\### 3. Add API keys

Create a .env file in the project root:

GEMINI\_API\_KEY=your\_gemini\_key\_here

GROQ\_API\_KEY=your\_groq\_key\_here



\### 4. Run

python classifier.py



\## Models Used

\- Primary: gemini/gemini-2.5-flash (Google Gemini free tier)

\- Fallback: groq/llama-3.3-70b-versatile (Groq free tier)

