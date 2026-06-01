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

![Wicket-Company Demo]
Welcome to Wicket-Company v3.3 (Butter-Smooth, Hireable, Company-Grade) — type 'exit' to bolt!
Type 'help' for a spot of guidance, any time.

Your Wicket-Company welcome:
No calendar events.
Atmosphere: Breezy, 64°F
No to-dos left.
Last note: No notes yet.
Opening jest: Why was the computer cold? It forgot to close its Windows!

You: 1
➡️ -- Website/SEO Manager --
Home page URL [ ] : https://acme-storage.com
Main SEO keywords (comma-separated) [ ]: storage, automation, analytics
Site description [ ] : Secure, scalable storage management for modern teams
✔️ Website content updated.

You: 2
➡️ -- Reporting/Data Entry --
Team [ops]: marketing
Entry category [task]: campaign launch
Describe the entry: Launched 2026 spring promo.
✔️ Entry logged.
ℹ️ Entries logged: 1

You: 3
➡️ -- Marketing Campaign Tracker --
Campaign name: Spring Sale
Landing page headline: Save Big This Spring!
UTM tag (e.g., utm_campaign): spring2026
Landing page URL: https://acme-storage.com/spring
✔️ Marketing campaign added.

You: 4
➡️ -- Notes --
Add a new note (or Enter to skip): Remember to A/B test signup form.
✔️ Note added.
ℹ️ Recent notes:
- [2026-06-01 13:15] Remember to A/B test signup form.

You: 5
➡️ -- Toolbox Analytics --
Website Home URL: https://acme-storage.com
SEO Keywords: storage, automation, analytics
Site Description: Secure, scalable storage management for modern teams
Entries logged: 1
Marketing campaigns: 1
Total notes: 1
Total files: 0
Session time: 2026-06-01 13:16
👀 Looking for a dev to build and maintain tools like this? Contact Adam Clark — savagetism@icloud.com — github.com/savageAZfck

Export entries as CSV? [n] y
✔️ Entries exported to entries_export.csv.

You: ai copilot
➡️ -- AI Copilot (Demo Only) --
What would you like AI to help with? (seo, content, code) Generate catchy headline for summer promo.
🤖 Thinking...
✔️ "Unlock Summer Savings with ACME Storage!"

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
- Total Interactions: 8

You: exit
Wicket Analytics (tea served upon request):
- ...
Cheerio from Wicket-Company 🫖

---

## ✨ Example Usage

