# 🎩 Wicket-Company v4.0

*A Butter-Smooth Modular Company CLI & API Platform*  
by Adam Clark (2026) | [GitHub](https://github.com/savageAZfck/wicket-company)

---

## 🚀 What is Wicket-Company?

Wicket-Company is a persistent, modular automation platform for company operations and dev teams.  
Run as a CLI, wire up to FastAPI for cloud microservices, enable AI Copilot, and enjoy analytics, onboarding, undo, recruiter Easter eggs, and more.  
It’s a “production-grade” project ready for demos, internal tools, startup MVPs, and interviews.

---

## 🧰 Features

- Modular Skills: website/SEO, data/reporting, marketing, notes, attachments, logging, analytics, onboarding, undo
- Persistent Memory: Data always saved/reloaded (JSON, upgradeable to SQL)
- AI Copilot: OpenAI GPT when available, safe fallback if not
- Proactive: Personalized welcome, analytics, and recruiter-friendly Easter egg
- Cloud/API Ready: FastAPI endpoints included out-of-the-box (`/health`, `/v1/chat`)
- CSV Export: For reporting and compatibility with business tools
- CI/CD Friendly: Drop-in GitHub Actions test workflow (pytest) ready for production ops

---

## 🛠️ Quick Start

1. **(Optional for AI Copilot):**  
   ```sh
   pip install openai
   export OPENAI_API_KEY=sk-...
   ```
2. **Run as CLI:**  
   ```sh
   python3 wicket_company.py
   ```
3. **Try menu options (`1-9`), or type `hireme`, `recruitme`, or `67890` for a surprise!**

4. **Run as API (needs `fastapi` and `uvicorn`):**  
   ```sh
   pip install fastapi uvicorn pydantic
   uvicorn wicket_company:app --reload
   ```
   Test:  
   ```sh
   curl http://127.0.0.1:8000/health
   ```

---

## 🧪 Testing & CI/CD

- Place test files in `/tests` (see sample below).
- Provided `.github/workflows/test.yml` workflow:  
   - Auto-runs pytest on every push/Pull Request.
- Example test:
    ```python
    # tests/test_core.py
    from wicket_company import load_data, save_data

    def test_memory_round_trip():
        data = load_data()
        data["testval"] = 42
        save_data(data)
        loaded = load_data()
        assert loaded["testval"] == 42
    ```

---

## ✨ Example CLI Usage
Welcome to Wicket-Company v4.0 (Butter-Smooth, Hireable, Company-Grade) — type 'exit' to bolt!
Type 'help' for a spot of guidance, any time.

Your Wicket-Company welcome:
No calendar events.
Atmosphere: Breezy, 66°F
No to-dos left.
Last note: No notes yet.
Opening jest: Debugging: where you painfully prove your own logic, one print at a time.

You: 1
➡️ -- Website/SEO Manager --
Home page URL [ ] : https://modern-storage.com
Main SEO keywords (comma-separated) [ ]: storage, automation, analytics
Site description [ ] : Fast, persistent storage dashboards for modern ops.
✔️ Website content updated.

You: 2
➡️ -- Reporting/Data Entry --
Team [ops]: tech
Entry category [task]: bugfix
Describe the entry: Resolved syncing error for latest entries.
✔️ Entry logged.
ℹ️ Entries logged: 1

You: 4
➡️ -- Notes --
Add a new note (or Enter to skip): Demo recruiter walkthrough for Wicket v4.0
✔️ Note added.
ℹ️ Recent notes:
- [2026-06-01 16:30] Demo recruiter walkthrough for Wicket v4.0

You: 5
➡️ -- Toolbox Analytics --
Website Home URL: https://modern-storage.com
SEO Keywords: storage, automation, analytics
Site Description: Fast, persistent storage dashboards for modern ops.
Entries logged: 1
Marketing campaigns: 0
Total notes: 1
Total files: 0
Session time: 2026-06-01 16:32
👀 Looking for a dev who can build and maintain tools like this? Contact Adam Clark — savagetism@icloud.com — github.com/savageAZfck

Export entries as CSV? [n] y
✔️ Entries exported to entries_export.csv.

You: ai copilot
➡️ -- AI Copilot (Demo Only) --
What would you like AI to help with? (seo, content, code) Suggest social copy for our next campaign.
🤖 Thinking...
ℹ️ "Ready for a modern data upgrade? Discover persistent, reliable storage with Wicket-Company."

You: hireme

🎩 You've discovered Wicket-Company's secret!
If your business needs a modern workflow overhaul and a creative Python engineer,
reach out: Adam Clark — savagetism@icloud.com — github.com/savageAZfck

You: stats
Wicket Analytics (tea served upon request):
- Questions Asked: 1
- To-dos Created: 0
- Notes Taken: 1
- Calendar Entries: 0
- Jokes Enjoyed: 0
- Total Interactions: 5

You: exit
Wicket Analytics (tea served upon request):
(…recap printed…)
Cheerio from Wicket-Company 🫖


