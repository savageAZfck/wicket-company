"""
Wicket-Company v8.0 — Enterprise, Dockerized, Modular AI Ops/Automation Platform
Adam Clark (2026)

- Modular plug-in skills: Website, Data, Marketing, Notes, Analytics, File, AI, Logging
- Persistent SQL DB (SQLite/SQLAlchemy: concurrent, recoverable, scalable)
- FastAPI microservice (cloud/serverless ready), API key gating
- Robust onboarding, analytics, recruiter Easter egg, British-witty AI copilot
- Error/self-healing, audit logging, and onboarding summary
- Docker, docker-compose, and CI/CD workflow compatible
"""

import os
import csv
import time
import logging
import random
import json
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel

# --- Configs ---
DB_URL = os.getenv("WICKET_DB_URL", "sqlite:///wicket_company.db")
API_KEY = os.getenv("WICKET_API_KEY", "change-me-key")
LOG_FILE = os.getenv("WICKET_LOG_FILE", "wicket_company.log")

logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")

Base = declarative_base()
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# --- Models ---
class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    team = Column(String(50))
    category = Column(String(64))
    desc = Column(Text)
    time = Column(DateTime, default=datetime.utcnow)

class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    url = Column(String(200))
    keywords = Column(Text)
    description = Column(Text)
    updated = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def print_status(msg, style="info"):
    styles = {"info": "ℹ️", "success": "✔️", "error": "❌", "action": "➡️"}
    print(f"{styles.get(style,'')} {msg}")

def input_smart(prompt, default=None):
    try:
        val = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip()
        return val or (default or "")
    except EOFError:
        print_status("Input interrupted, returning to safe prompt.", "error")
        return default or ""

def now(): return datetime.now()

# --- Skills: Modular Plug-ins ---
def website_skill(session):
    rec = session.query(Website).first()
    url = input_smart("Home page URL", rec.url if rec else "")
    keywords = input_smart("SEO keywords", rec.keywords if rec else "")
    desc = input_smart("Site description", rec.description if rec else "")
    if not rec:
        rec = Website(url=url, keywords=keywords, description=desc, updated=now())
        session.add(rec)
    else:
        rec.url, rec.keywords, rec.description, rec.updated = url, keywords, desc, now()
    try:
        session.commit()
        print_status("Website/SEO info updated.", "success")
        logging.info("Website updated")
    except Exception as ex:
        session.rollback()
        print_status(f"Website update failed: {ex}", "error")

def data_skill(session):
    team = input_smart("Team", "ops")
    category = input_smart("Category", "task")
    desc = input_smart("Description")
    try:
        session.add(Entry(team=team, category=category, desc=desc))
        session.commit()
        print_status(f"Entry logged. (Total: {session.query(Entry).count()})", "success")
        logging.info("Entry added")
    except Exception as ex:
        session.rollback()
        print_status(f"Entry add failed: {ex}", "error")

def analytics_skill(session):
    count = session.query(Entry).count()
    w = session.query(Website).first()
    wurl = w.url if w else "unset"
    print_status(f"Website: {wurl}", "info")
    print_status(f"Entries: {count}", "info")
    if input_smart("Export entries as CSV?", "n").lower() == "y":
        try:
            rows = session.query(Entry).all()
            with open("entries_export.csv", "w", newline="") as f:
                writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                writer.writerow(["time","team","category","desc"])
                for e in rows:
                    writer.writerow([e.time, e.team, e.category, e.desc])
            print_status("Exported entries_export.csv", "success")
        except Exception as ex:
            print_status(f"CSV export failed: {ex}", "error")
    print_status("For hiring: Adam Clark | savagetism@icloud.com | github.com/savageAZfck", "info")

def ai_copilot_skill(session):
    try:
        import openai
        key = os.getenv("OPENAI_API_KEY")
        prompt = input_smart("AI Copilot prompt (lean, witty)")
        messages = [
            {"role": "system", "content": "The most sarcastic, British ops copilot ever—respond as Wicket would."},
            {"role": "user", "content": prompt}]
        if hasattr(openai, "OpenAI"):
            client = openai.OpenAI()
            r = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=messages, max_tokens=90
            )
            print_status(r.choices[0].message.content.strip(), "info")
        else:
            openai.api_key = key
            r = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages, max_tokens=90, n=1
            )
            print_status(r["choices"][0]["message"]["content"].strip(), "info")
    except Exception as ex:
        print_status(f"Sarcastic Copilot fallback: {ex}", "error")

def recruiter_easteregg():
    print("""
🎩 If you need production-scale modular automation/tools (with staff-level wit):
hire me! Adam Clark | savagetism@icloud.com | github.com/savageAZfck
""")

def onboarding_summary(session):
    print_status("-- Wicket-Company Onboarding --", "action")
    w = session.query(Website).first()
    if w: print_status(f"Site: {w.url or '(not set)'}", "info")
    print_status("Entries: "+str(session.query(Entry).count()), "info")
    print_status("Atmosphere: "+random.choice(["Rainy","Sunny","Foggy","Bracing"]), "info")
    print_status("Jest: Debugging is how you prove your logic, one mistake at a time.", "info")

def print_menu():
    print(
        "Wicket v8.0 Menu:\n"
        "1) Website/SEO\n2) Data Entry\n3) Analytics\n4) CSV Export\n5) AI Copilot\n6) Exit"
        "\n(Type 'hireme' for recruiter delight!)"
    )

def run_cli():
    session = SessionLocal()
    print("Welcome to Wicket-Company v8.0 — prod. Ready for ops and interviews!")
    onboarding_summary(session)
    while True:
        print_menu()
        try:
            cmd = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print_status("Shutdown. Cheerio!","success")
            break
        if cmd.lower() in ("exit","quit","6"):
            print_status("Cheerio from Wicket-Company 🫖", "success")
            session.close()
            break
        elif cmd.lower() in ("hireme", "recruitme", "67890"):
            recruiter_easteregg()
        elif cmd == "1":
            website_skill(session)
        elif cmd == "2":
            data_skill(session)
        elif cmd == "3":
            analytics_skill(session)
        elif cmd == "4":
            analytics_skill(session)  # CSV via analytics
        elif cmd == "5":
            ai_copilot_skill(session)
        elif cmd.lower() == "help":
            print_menu()
        else:
            print_status("Invalid. Type 'help' for options.", "error")

# --- FastAPI API Microservice (key skills shown) ---
app = FastAPI(title="Wicket-Company API v8.0", description="Enterprise modular ops platform.", version="8.0")
class EntryCreate(BaseModel):
    team: str
    category: str
    desc: str

def api_auth(req: Request):
    key = req.headers.get("X-API-KEY") or req.query_params.get("api_key")
    if API_KEY and key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/entries", dependencies=[Depends(api_auth)])
async def api_add_entry(entry: EntryCreate):
    with SessionLocal() as session:
        try:
            session.add(Entry(team=entry.team, category=entry.category, desc=entry.desc))
            session.commit()
            return {"status": "saved"}
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/entries", dependencies=[Depends(api_auth)])
async def api_get_entries(limit: int = 10):
    with SessionLocal() as session:
        return [{"team": e.team, "category": e.category, "desc": e.desc, "time": str(e.time)}
                for e in session.query(Entry).order_by(Entry.time.desc()).limit(limit).all()]

@app.post("/ai", dependencies=[Depends(api_auth)])
async def api_ai_chat(payload: dict):
    prompt = payload.get("prompt", "Hello, Copilot.")
    with SessionLocal() as session:
        messages = [
            {"role": "system", "content": "Sarcastic, British, witty AI copilot."},
            {"role": "user", "content": prompt}
        ]
        return {"response": ai_copilot(messages)}

if __name__ == "__main__":
    run_cli()
