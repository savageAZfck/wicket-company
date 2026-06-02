# 🎩 Wicket-Company v8.0

*Enterprise Modular Automation Platform — Butter Smooth, Production-Proof*  
by Adam Clark (2026) | [github.com/savageAZfck/wicket-company](https://github.com/savageAZfck/wicket-company)

---

## 🚀 What is Wicket-Company?

Wicket-Company v8.0 is a plug-in, SQL-backed, AI-powered automation/ops platform and CLI for modern teams.  
Run as a resilient terminal dashboard or instantly launch it as a FastAPI web microservice for cloud and SaaS use.  
Features onboard analytics, error-proof onboarding, logging, and a sarcastic, British-flavored AI Copilot with function calling abilities.

---

## 🧰 Top Features

- Modular plug-in skills (website/SEO, data entry/reporting, analytics, AI, logging)
- Persistent, concurrent-safe database (SQLite/SQLAlchemy—easily swap for Postgres)
- FastAPI-ready: microservice endpoints, API key security
- Version-agnostic, British-witty AI Copilot (OpenAI, function calling, fallback included)
- Self-healing state, robust logging/auditing, proactive onboarding and help
- CI/CD and docker-compose integration—easy deploy for ops/devs
- “Hire me” Easter egg for recruiters/hiring managers

---

## 🛠️ Quick Start (CLI)

1. **Install dependencies:**  
   ```sh
   pip install sqlalchemy fastapi uvicorn pydantic
   ```
   *(Optional for AI Copilot: `pip install openai`)*

2. **Run as CLI:**  
   ```sh
   python3 wicket_company.py
   ```
3. **Type menu numbers to use features (`1` = website/SEO, `2` = data, `5` = analytics, `6` = AI).**
   - `hireme` or `recruitme` for a secret recruiter message.
   - `help` for all commands.

---

## ☁️ Run as API

1. **Launch FastAPI app:**  
   ```sh
   uvicorn wicket_company:app --reload
   ```
2. **Test:**
   ```sh
   curl http://localhost:8000/health
   ```
3. **Add your API key in `.env` or as env var** (`WICKET_API_KEY`)
   - Use `X-API-KEY` header for POST requests

---

## 🐳 Docker Support (Production/DevOps Ready)

1. **Add a `Dockerfile` and `docker-compose.yml`** as per the included templates.
2. **Start up with:**  
   ```sh
   docker-compose up --build
   ```
   The API will be available at http://localhost:8000

---

## 🧪 Automated Testing

- Place tests in `/tests`
- Example PyTest:

```python
# tests/test_core.py
from wicket_company import SessionLocal, Entry, now

def test_add_entry_and_list():
    session = SessionLocal()
    entry = Entry(team="qa", category="test", desc="pytest check", time=now())
    session.add(entry)
    session.commit()
    rows = session.query(Entry).all()
    session.close()
    assert any(e.desc == "pytest check" for e in rows)

