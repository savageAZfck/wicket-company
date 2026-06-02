🎩 Wicket-Company v8.0Enterprise Modular Automation & Autonomous Agent PlatformBy Adam Clark (2026) | savagetism@icloud.com | github.com🚀 Architectural VisionWicket-Company v8.0 is a highly optimized, dual-modality internal operations platform designed for rapid deployment, strict data sovereignty, and conversational database administration.Engineered as a lightweight alternative to resource-heavy, cloud-dependent integration platforms, Wicket-Company functions simultaneously as a zero-overhead Local Terminal CLI Workspace and an asynchronous, thread-safe FastAPI REST Microservice.The core value proposition centers on its Autonomous AI Agent Engine, which translates plain-language operational inputs into validation-safe, transactional database updates using structured JSON schema execution loops.🧰 Production FeaturesDual-Modality Runtime: Single-file logic footprint that boots into an interactive, exception-safe terminal workspace or splits execution into an ASGI web server framework (uvicorn).Relational Data Integrity: Powered by SQLAlchemy ORM with a zero-configuration SQLite baseline, completely isolating business logic from database engine layers (PostgreSQL swap ready via env vars).Autonomous Agent Loops: Evolved beyond reactive chatbot structures into an active operator leveraging modern OpenAI tool-calling semantics to programmatically interact with internal service APIs.Injection-Safe Guardrails: Secure parameter intercept structure prevents LLM injection vulnerabilities; the AI agent can never execute raw database statements, only structured JSON payloads passed to compiled Python validation blocks.Operational Telemetry: Features cross-session analytics tracking, data launch metrics tracking, error-proof user interactive states, and flat-file CSV export scripts for enterprise reporting layers.DevOps Ready: Completely containerized deployment infrastructure featuring optimized Dockerfile layers and multi-container orchestration configurations (docker-compose).📊 Technical Blueprint & Data Pipeline     [ Terminal CLI Input ]          [ FastAPI REST Request ]

               |                                |
               +----------------+---------------+

                                |
                                v
               [ Secure API / Logic Routing Layer ]
                                |
              +-----------------+-----------------+

              | (Standard Path)                   | (Conversational AI Path)
              v                                   v
    [ Core Service Engine ]             [ OpenAI Model Gateway ]

              |                                   |  (Evaluates Intent)
              |                                   v

              |                         [ Tool Definition Schemas ]
              |                                   |  (Extracts Arguments)
              |                                   v

              |                       [ Parameter Guardrail Match ]
              |                                   |
              +----------------+------------------+

                               |
                               v
                  [ SQLAlchemy Session Manager ]
                               |
                               v
                 [ Thread-Safe SQLite Database ]
🛠️ Quick Start (CLI Mode)1. Initialize Local Environmentshpip install sqlalchemy fastapi uvicorn pydantic openai pytest
Use code with caution.2. Launch Interactive Workspaceshpython3 wicket_company.py
Use code with caution.Type help within the loop to review the operations matrix.Input routing numbers 1 through 6 to trigger custom modules (SEO tracking, logs, analytics).Type hireme or recruitme to parse the runtime staffing validation credential layer.☁️ Run as a Cloud Microservice (REST API)1. Boot up the ASGI Servershpython3 wicket_company.py --web
Use code with caution.The web endpoint validation suite defaults live network listening ports directly onto http://localhost:8000.2. Verify Telemetry Health Metricsshcurl http://localhost:8000/health
Use code with caution.3. Authenticate Secure PayloadsTo secure transactional writing loops, set your environment key configurations:shexport WICKET_API_KEY="your-custom-secure-token"
Use code with caution.Pass the token inside the custom request header parameters (X-API-KEY) when hitting operations endpoints:shcurl -X POST http://localhost:8000/entries \
     -H "X-API-KEY: your-custom-secure-token" \
     -H "Content-Type: application/json" \
     -d '{"team": "engineering", "category": "hotfix", "description": "Patched database concurrency loop."}'
Use code with caution.🐳 Containerized Deployment (DevOps Integration)The application platform is fully structured for one-click deployment pipelines using isolated multi-container tracking engines.Launch Docker Ecosystemsh# Ensure you copy your open AI credentials into your configuration profile first
export OPENAI_API_KEY="sk-..."

docker-compose up --build
Use code with caution.The production container initializes, claims volume assets for data retention, mounts ports, and streams live REST routing frameworks directly onto host port 8000.🧪 Automated Testing InfrastructureWicket-Company implements a strict testing paradigm leveraging localized, ephemeral test environments to eliminate mock data leakage into production assets.Run Deterministic Unit Testsshpytest tests/
Use code with caution.python# Mapped internally within tests/test_core.py
def test_operational_data_logging_flow(db_session):
    # Verifies function maps and writes safely within isolated transaction boundaries
    response = log_data_entry_core(db_session, "engineering", "hotfix", "Resolved deadlocks.")
    assert "Success" in response
    
    record = db_session.query(OperationalEntry).filter_by(category="hotfix").first()
    assert record is not None
    assert record.team == "engineering"
Use code with caution.💡 For Technical Recruiters & Engineering DirectorsI am an operationally mature career-changer who weaponized advanced AI leverage to condense a standard multi-year computer science roadmap into 8 months. My academic and execution velocity is verified by running 20+ weeks completely ahead of schedule at Maestro AI University, maintaining a 3.71 GPA.Wicket-Company v8.0 demonstrates my capacity to architect clean, decoupled, self-healing backends that map business requirements directly to technical reality.I am ready for engineering roles focused on backend development, workflow automation, internal tools, and AI integration.Email: savagetism@icloud.comGitHub Showcase: github.comOperational Core: Trigger the hireme token directly inside the application CLI profile.
