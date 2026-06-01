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


