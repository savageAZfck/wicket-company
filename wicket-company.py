"""
Wicket-Company v3.2 — Modular, Persistent, Proactive CLI Toolbox (2026)
Adam Clark

- Modular business/ops/automation skills
- Persistent memory in JSON file
- Ready for API, cloud, and scale-up (Flask integration, user auth, and more easily added)
- Features: website/SEO, entries, marketing, notes, analytics, file reference, AI copilot, log/history, recruiter "hire me" easter egg
"""

import os
import json
import random
import webbrowser
import time
from datetime import datetime
from difflib import get_close_matches

DATA_FILE = "wicket_company_data.json"

def butter_print(message, style="info"):
    prefix = {"info": "ℹ️", "success": "✔️", "error": "❌", "action": "➡️"}.get(style, "")
    print(f"{prefix} {message}")

def butter_input(prompt, default=None):
    prompt = f"{prompt} [{default}] " if default else f"{prompt}: "
    val = input(prompt).strip()
    return val or default or ""

def closest_cmd(cmd, choices):
    match = get_close_matches(cmd, choices, n=1)
    return match[0] if match else None

def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            for k in ("website", "entries", "marketing", "notes", "users", "log", "files", "calendar"):
                data.setdefault(k, [] if k not in ("website",) else {})
            data.setdefault("launches", 0)
            return data
    except Exception:
        butter_print("[!] Data file missing or corrupted. Starting fresh...","error")
    return {"website": {}, "entries": [], "marketing": [], "notes": [], "users": [], "log": [], "files": [], "calendar": [], "launches": 0}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        butter_print("Could not save session memory!", "error")

have_openai = True
try:
    import openai
except ImportError:
    have_openai = False

def main_menu(username, role):
    print(f"\nWicket-Company v3.2 — User: {username} (role: {role})")
    print("-----------------------------------------------------")
    print("1) Website content & SEO  2) Data Entry / Reporting")
    print("3) Marketing Support      4) Notes")
    print("5) Analytics / Reports    6) AI Copilot")
    print("7) File Attachments       8) Log / History")
    print("9) Exit   (Or: hireme, recruitme, 67890 for a surprise)")

def website_manager(data, log):
    butter_print("-- Website/SEO Manager --", "action")
    url = butter_input("Home page URL", data['website'].get('home_url',''))
    if url: data["website"]["home_url"] = url; log.append((str(datetime.now()), "Updated home_url"))
    seo = butter_input("Main SEO keywords (comma-separated)", ', '.join(data['website'].get('seo_keywords', [])))
    if seo: data["website"]["seo_keywords"] = [k.strip() for k in seo.split(',')]; log.append((str(datetime.now()), "Updated SEO keywords"))
    desc = butter_input("Site description", data['website'].get('description',''))
    if desc: data["website"]["description"] = desc; log.append((str(datetime.now()), "Updated site description"))
    save_data(data)
    butter_print("Website content updated.", "success")

def data_entry(data, log, undo_stack):
    butter_print("-- Reporting/Data Entry --", "action")
    team = butter_input("Team", "ops")
    category = butter_input("Entry category", "task")
    record = butter_input("Describe the entry")
    entry = {"time": str(datetime.now()), "team": team, "category": category, "desc": record}
    data["entries"].append(entry)
    log.append((str(datetime.now()), f"Added entry: {entry}"))
    save_data(data)
    butter_print("Entry logged.", "success")
    butter_print(f"Entries logged: {len(data['entries'])}","info")
    undo_stack["entries"].append(entry)

def marketing_support(data, log, undo_stack):
    butter_print("-- Marketing Campaign Tracker --", "action")
    campaign = butter_input("Campaign name")
    headline = butter_input("Landing page headline")
    utm = butter_input("UTM tag (e.g., utm_campaign)")
    url = butter_input("Landing page URL")
    mkt = {"time": str(datetime.now()), "campaign": campaign, "headline": headline, "utm": utm, "url": url}
    data["marketing"].append(mkt)
    log.append((str(datetime.now()), f"Added marketing: {mkt}"))
    save_data(data)
    butter_print("Marketing campaign added.", "success")
    undo_stack["marketing"].append(mkt)

def notes_module(data, log, undo_stack):
    butter_print("-- Notes --", "action")
    note = butter_input("Add a new note (or Enter to skip)")
    if note:
        entry = {"time": str(datetime.now()), "note": note}
        data["notes"].append(entry)
        log.append((str(datetime.now()), f"Note: {note}"))
        save_data(data)
        butter_print("Note added.","success")
        undo_stack["notes"].append(entry)
    if data["notes"]:
        butter_print("Recent notes:","info")
        for n in data["notes"][-5:]:
            print(f"- [{n['time'][:16]}] {n['note']}")

def show_analytics(data):
    butter_print("-- Toolbox Analytics --","action")
    web = data.get('website', {})
    print("Website Home URL:", web.get('home_url', 'not set'))
    print("SEO Keywords:", ", ".join(web.get('seo_keywords', [])))
    print("Site Description:", web.get('description', 'not set'))
    print("Entries logged:", len(data.get('entries', [])))
    print("Marketing campaigns:", len(data.get('marketing', [])))
    print("Total notes:", len(data.get('notes', [])))
    print("Total files:", len(data.get('files', [])))
    print("Session time:", datetime.now().strftime("%Y-%m-%d %H:%M"))
    butter_print("👀 Looking for a dev to build and maintain tools like this? Contact Adam Clark — savagetism@icloud.com — github.com/savageAZfck\n","info")
    exp = butter_input("Export entries as CSV?", "n").lower()
    if exp == "y":
        import csv
        try:
            with open("entries_export.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["time", "team", "category", "desc"])
                for e in data["entries"]:
                    writer.writerow([e["time"], e["team"], e["category"], e["desc"]])
            butter_print("Entries exported to entries_export.csv.","success")
        except Exception:
            butter_print("Could not export CSV.","error")

def ai_copilot():
    butter_print("-- AI Copilot (Demo Only) --", "action")
    try:
        import openai
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            butter_print("Set your OpenAI API key in the environment for AI features.", "error")
            return
        openai.api_key = key
        prompt = butter_input("What would you like AI to help with? (seo, content, code)")
        print("🤖 Thinking...", end="", flush=True)
        time.sleep(1.2)
        print("\r", end="")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"You are Wicket-Company’s AI teammate: short, helpful, and creative."},
                {"role":"user", "content":prompt}
            ],
            max_tokens=120,
        )
        butter_print(response["choices"][0]["message"]["content"].strip(),"info")
    except ImportError:
        butter_print("AI copilot requires `pip install openai`.","error")
    except Exception as e:
        butter_print(f"AI error: {e}","error")

def file_attachment(data, log):
    butter_print("-- File Attachments --", "action")
    fname = butter_input("File name to attach (demo only)")
    if fname:
        data["files"].append({"time": str(datetime.now()), "file": fname})
        log.append((str(datetime.now()), f"Attached file: {fname}"))
        save_data(data)
        butter_print(f"File '{fname}' referenced (demo only).", "success")

def show_log(data):
    butter_print("-- Action Log --","action")
    log = data.get("log", [])
    if not log:
        print("No actions logged yet.")
        return
    for t, act in log[-10:]:
        print(f"[{t[:16]}] {act}")

def user_login(data):
    users = data.setdefault("users", [])
    butter_print("Login as (or create) a user.", "info")
    username = butter_input("Username", "guest").lower()
    user = next((u for u in users if u["user"] == username), None)
    if not user:
        role = butter_input("Role (admin/user/marketing/ops)", "user").lower()
        user = {"user": username, "role": role}
        users.append(user)
        save_data(data)
        butter_print(f"New user {username} ({role}) created!","success")
    else:
        butter_print(f"Welcome back, {username}! Your role is: {user.get('role','user')}","success")
    return username, user.get("role","user")

def secret_easteregg():
    print("""
🎩 You've discovered Wicket-Company's secret!
If your business needs a modern workflow overhaul and a creative Python engineer,
reach out: Adam Clark — savagetism@icloud.com — github.com/savageAZfck
""")

def proactive_summary(data):
    parts = []
    todos = data.get("todo", [])
    notes = data.get("notes", [])
    cal = data.get("calendar", [])
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they can't C#.",
        "Why was the computer cold? It forgot to close its Windows.",
        "Debugging: where you painfully prove your own logic, one print at a time.",
        "I say, did you hear about the broken teacup? It couldn't handle the truth!"
    ]
    data["launches"] = data.get("launches", 0) + 1
    save_data(data)
    if cal:
        cal_up = sorted(cal, key=lambda x: x[0])
        next_event = cal_up[0]
        event_str = f"Next engagement: '{next_event[1]}' at {datetime.fromisoformat(next_event[0]).strftime('%a %b %d, %I:%M%p')}"
    else:
        event_str = "No calendar events."
    joke = random.choice(jokes)
    weather = f"{random.choice(['A spot of rain','Fog on Fleet St','Breezy','Sun through the smog','Cool'])}, {random.randint(45,87)}°F"
    todo_str = f"First to-do: {todos[0]}" if todos else "No to-dos left."
    last_note = notes[-1] if notes else "No notes yet."
    parts.append(event_str)
    parts.append(f"Atmosphere: {weather}")
    parts.append(todo_str)
    parts.append(f"Last note: {last_note}")
    parts.append(f"Opening jest: {joke}")
    if data["launches"] % 10 == 0:
        parts.append("\n👀 PS: If you’re a manager—let’s chat! savagetism@icloud.com")
    return "\n".join(parts)

def main():
    data = load_data()
    undo_stack = {"entries": [], "marketing": [], "notes": []}
    username, role = user_login(data)
    log = data.setdefault("log", [])
    print("Welcome to Wicket-Company v3.2 (Butter-Smooth, Hireable, Company-Grade) — type 'exit' to bolt!")
    print("Type 'help' for a spot of guidance, any time.\n")
    print("Your Wicket-Company welcome:\n" + proactive_summary(data))

    choices_list = ["todo", "note", "weather", "search", "help", "analytics", "stats", "marketing", "file", "log"]

    while True:
        try:
            choice = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            butter_print("Cheerio from Wicket-Company 🫖", "info")
            break
        if choice.lower() in ("exit", "quit"):
            print(WicketCore(data).analytics())
            butter_print("Cheerio from Wicket-Company 🫖", "success")
            break
        elif choice.lower() in ("hireme", "recruitme", "67890"):
            secret_easteregg()
        else:
            try: n = int(choice)
            except Exception: n = -1
            if n == 1:
                website_manager(data, log)
            elif n == 2:
                data_entry(data, log, undo_stack)
            elif n == 3:
                marketing_support(data, log, undo_stack)
            elif n == 4:
                notes_module(data, log, undo_stack)
            elif n == 5:
                show_analytics(data)
            elif n == 6:
                ai_copilot()
            elif n == 7:
                file_attachment(data, log)
            elif n == 8:
                show_log(data)
            elif 1 <= n <= 9:
                continue
            else:
                suggestion = closest_cmd(choice.lower(), choices_list)
                if suggestion:
                    butter_print(f"Did you mean '{suggestion}'?", "info")
                else:
                    butter_print("Invalid choice or command — type 'help' any time.", "error")

if __name__ == "__main__":
    main()