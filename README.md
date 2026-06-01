# 🎩 Wicket-Company v3.3

*A Butter-Smooth Modular Company CLI & API Toolbox*  
by Adam Clark (2026) | [GitHub](https://github.com/savageAZfck/wicket-company)

---

## 🚀 What is Wicket-Company?

Wicket-Company is a persistent, modular business automation toolbox built for modern operations, dev teams, SMBs, and startups.  
Designed “builder-first,” it’s ready for automation, analytics, AI, and cloud integration—plus it’s got playful, memorable UX for both teams and recruiters.

---

## 🧰 Features

- **Modular Skills:**  
  - Website & SEO manager
  - Internal data entry & reporting
  - Marketing campaign tracker
  - Notes with undo/history
  - Proactive onboarding and analytics (summary/dashboard)
  - AI Copilot (OpenAI GPT-3.5/4, or fallback chat)
  - File/reference tracking
  - Multi-user support (username/role)
  - Logging/history (with last actions)
  - CSV export for reporting
  - Error proof, self-healing data (robust JSON backup)
  - Recruiter “Easter egg” (`hireme`/`recruitme`/`67890`)

- **Persistency:**  
  - All sessions, to-dos, campaigns, notes, and usage stats are stored in `wicket_company_data.json`

- **Cloud/API Ready:**  
  - Easily import into FastAPI for cloud microservice or web UI extension
  - “Skill” modules are plug-and-play—add new APIs, endpoints, or automation as needed

- **CI/CD Friendly:**  
  - Comes with sample GitHub Actions workflow (`.github/workflows/test.yml`) for automatic testing

---

## 🛠️ Quick Start

1. **Install dependencies**  
   *(Optional, for AI copilot)*  
   ```sh
   pip install openai
   ```
2. **Run as CLI:**  
   ```sh
   python3 wicket_company.py
   ```

3. **First time?**  
   - Log in or create a new user (usernames/roles supported)
   - You’re greeted with a personalized summary/dashboard on launch

4. **Try sample features:**  
   - `1`, `2`, ... for menu options  
   - `todo add [task]`, `note add [text]`, `analytics`, or `hireme` for Easter egg  
   - Try `ai copilot` (option 6) if OpenAI key set as env (`export OPENAI_API_KEY=sk-...`)

---

## 🎞️ Demo

![Wicket-Company Demo](demo.gif)
*(Add your gif here!)*

---

## ✨ Example Usage

