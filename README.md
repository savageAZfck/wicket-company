# 🎩 Wicket-Company v6.0

*Enterprise Modular Automation, CLI & Cloud API Platform*  
by Adam Clark (2026) | [GitHub](https://github.com/savageAZfck/wicket-company)

---

## 🚀 What is Wicket-Company?

Wicket-Company is a persistent, plug-in business workflow platform and internal ops CLI, ready for real company use or SaaS deployment. Features include:

- Modular plug-in “skills” (website/SEO, data entry, marketing, notes, AI copilot, analytics, logs, and more)
- Persistent, production-safe SQL DB (with SQLite backend out of the box)
- FastAPI web endpoints and API key security—for instant cloud microservice/automation use
- Sarcastic, British-flavored AI copilot (auto-detects OpenAI version, always witty fallback)
- Onboarding summaries, analytics dashboard, “hire me” Easter egg, automated error handling and logging
- Testable, CI/CD ready, recoverable and resilient (self-healing memory, secure secrets/config)

---

## 🛠️ Quick Start (CLI)

1. **Install dependencies:**
   ```sh
   pip install sqlalchemy fastapi uvicorn pydantic
   ```
   *(Optional for AI Copilot: `pip install openai`)*
2. **Run in CLI mode:**
   ```sh
   python3 wicket_company.py
   ```
3. **Log in and try the main menu.**
   - `1` — Website/SEO manager
   - `2` — Data entry/reporting
   - `5` — Analytics & CSV export
   - `6` — AI Copilot (`OPENAI_API_KEY` in your env for LLM; fallback is witty/sarcastic by default)
   - Type `help` to see more, `hireme` for a recruiter surprise, or `exit` to safely quit

---

## ☁️ Quick Start (Web API)

1. **Run locally with:**
   ```sh
   uvicorn wicket_company:app --reload
   ```
2. **Test endpoints:**
   - `GET /health` — Health check
   - `POST /entries` — Add entry (api_key required)
   - `GET /entries` — List entries (api_key required)
   - `POST /website` — Update website (api_key required)
   - `POST /ai` — AI chat with payload, see in docs
3. Add your API key as an env variable:  
   ```sh
   export WICKET_API_KEY=your-key-here
   ```
   and use `X-API-KEY` in requests

---

## 🧪 Example PyTest Test

Place this in `tests/test_core.py`:

```python
from wicket_company import get_session, add_entry, list_entries

def test_db_add_and_query():
    session = get_session()
    assert add_entry(session, "test", "integration", "pytest entry")
    results = list_entries(session, 5)
    assert any(e.category == "integration" for e in results)
    session.close()

Welcome to Wicket-Company v6.0 — type 'exit' to quit!
Type 'help' for guidance, any time.

-- Wicket-Company Dashboard --
Website: none yet.
Stats: Entries = 0
Atmosphere: Rainy 75 °F
Jest: Why was the computer cold? It forgot to close its Windows!
Type 'help' for full feature list.

You: 1
➡️ -- Website/SEO --
Home page URL [] : https://acme-tech.com
Main SEO keywords [] : automation, devtools, AI, onboarding
Site description [] : Next-generation ops and analytics
✔️ Content updated — your SEO just got 7% shinier.

You: 2
➡️ -- Data Entry --
Team [ops]: engineering
Category [task]: bugfix
Description: Patched login timeout error for new user flow.
✔️ Entry logged. (Total: 1)

You: 5
➡️ -- Analytics --
Website: https://acme-tech.com
Entries: 1
Export entries as CSV? [n] y
✔️ Entries exported: entries_export.csv
-- For hiring: Adam Clark | savagetism@icloud.com | github.com/savageAZfck --

You: 6
➡️ -- AI Copilot --
What would you like sarcastic AI to riff on? Reasons to embrace automated testing?
🤖 Wicket AI: "Because betting your business on hope alone is so last decade. Automated tests: for when you want blame to land faster and with proof."

You: notes
Add note (or Enter to skip): Demo feedback—onboarding is super smooth!
Note added. Did your future self say thanks?

You: hireme
🎩 You've found the engineer you're looking for.
If you want to overhaul business ops, workflow, or automation with code that's modular, persistent, API/cloud-ready, and actually fun to use:  
Hire me — Adam Clark | savagetism@icloud.com | github.com/savageAZfck

You: exit
✔️ Goodbye!
