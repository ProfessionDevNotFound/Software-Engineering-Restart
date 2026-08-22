# Software-Engineering-Restart
A day-by-day, project-driven journey to rebuild my software engineering fundamentals and become a capable backend engineer. Learn → Recall → Build → Debug → Repeat.


### Week 1 — Python Revision + Project Skeleton
**Objective:** Comfortable reading/writing Python with functions, classes, exceptions, typing. First running FastAPI "Hello World."

- **Topics:** functions, classes, exceptions, type hints, virtual environments, packages, basic FastAPI route.
- **Mini-lessons:** one concept per session (see Section 8 for the crash course breakdown).
- **Mini-build:** by Day 3, a `Document` class with attributes (filename, upload date, tags). By Day 6, a FastAPI app with one GET route returning a hardcoded list of documents.
- **Project integration (v0):** this *is* the skeleton of the Personal Knowledge API — a bare FastAPI app that runs.
- **Recall without notes:** explain what a virtual environment does and why; write a function with a try/except from memory.
- **Checkpoint:** you can create a new FastAPI project from scratch, add one GET and one POST route, and explain what each does — without copy-pasting.

### Week 2 — HTTP/REST + PostgreSQL + SQL
**Objective:** Understand REST conventions; can write CRUD SQL; can connect Postgres to FastAPI.

- **Topics:** HTTP methods/status codes, REST resource conventions, JSON, SQL (SELECT/INSERT/UPDATE/DELETE/JOIN), primary/foreign keys, connecting Postgres via SQLAlchemy.
- **Mini-build:** a `documents` table in Postgres; a script that inserts and queries rows directly (before wiring to FastAPI).
- **Project integration (v1):** API + database — GET/POST routes now read/write real rows in Postgres instead of hardcoded data.
- **Recall:** explain primary vs foreign key out loud; write a JOIN query from memory.
- **Checkpoint:** you can create a table, write CRUD queries, use a JOIN, explain primary/foreign keys, and connect Postgres to FastAPI. Don't move on until this is true without looking things up.

### Week 3 — Users + Authentication
**Objective:** Register/login working; routes protected by JWT.

- **Topics:** password hashing (bcrypt/passlib), JWT structure, dependency injection in FastAPI (`Depends`), protecting routes.
- **Mini-build:** a `users` table; a `/register` and `/login` endpoint; a protected `/me` endpoint.
- **Project integration (v2):** users/authentication — documents now belong to a specific authenticated user.
- **Recall:** explain what a JWT contains and why it's not encrypted (just signed); explain what `Depends()` does in one sentence.
- **Checkpoint:** you can register a user, log in, get a token, and use it to access a protected route — and explain what happens at each step.

### Week 4 — File Uploads + Tags + Search
**Objective:** Users can upload PDF/TXT/MD/CSV, tag them, and search by keyword.

- **Topics:** FastAPI `UploadFile`, file storage (local disk is fine for Month 1), basic text extraction (plain read for txt/md/csv; a simple PDF text-extraction library for PDFs), SQL `ILIKE`/full-text search basics.
- **Mini-build:** an upload endpoint that stores a file and a metadata row; a search endpoint filtering by filename/tag/content keyword.
- **Project integration (v3 + v4):** file uploads, tagging, search — the core "knowledge" features are now real.
- **Recall:** explain the full upload flow (client → endpoint → validation → disk/db → response) without notes.
- **Checkpoint:** you can upload a file of each supported type, tag it, retrieve it, and find it via search.

### Week 5 — Testing, Logging, Error Handling
**Objective:** Confidence that the app behaves correctly, with visibility when it doesn't.

- **Topics:** pytest basics, testing FastAPI endpoints (`TestClient`), structured logging, consistent error responses (FastAPI exception handlers), input validation edge cases.
- **Mini-build:** pytest tests for register/login/upload/search; a custom exception handler returning consistent JSON errors.
- **Project integration (v5):** tests/logging/error handling — the app is now defensible, not just functional.
- **Recall:** explain what a good test actually verifies (not "it ran" — "it behaves correctly under X condition").
- **Checkpoint:** running `pytest` gives you a green suite covering the core flows; a bad request returns a sensible error, not a raw stack trace.

### Week 6 — Docker + Deployment
**Objective:** The whole app runs in containers and is reachable outside your machine.

- **Topics:** Dockerfile basics, Docker Compose (app + Postgres as two services), environment variables/secrets, a basic deployment target (Render/Railway/Fly.io — pick one free-tier option).
- **Mini-build:** a working `Dockerfile` + `docker-compose.yml`; the app running via `docker compose up`.
- **Project integration (v6 + v7):** Docker, deployment — final Month-1 state.
- **Recall:** explain what Docker Compose is doing versus running two `docker run` commands manually.
- **Checkpoint:** a stranger with your GitHub repo and a `.env.example` can run `docker compose up` and hit your API. That's the actual finish line.

*(If Week 6 needs to become Weeks 6–7, that's fine — deployment friction is normal, not a sign you're behind.)*

---

## 6. Daily Micro-Learning System (Normal Day)

| Session | Length | What |
|---|---|---|
| 1. Learn | 10–20 min | One concept only. Close the tab when done. |
| 2. Recall | 5–10 min | Explain it out loud/in writing, no notes. |
| 3. Code | 15–20 min | Tiny isolated exercise for that concept. |
| 4. Project | 15–20 min | Apply it directly inside the Personal Knowledge API. |
| 5. Review | 5–10 min | Quick note: what you learned, what's still fuzzy. |

Total: ~50–80 minutes, broken into pieces — never one continuous block.

---

## 7. Minimum / Normal / High-Energy Days

- **Minimum day (~20 min):** Session 2 (recall yesterday's concept) + Session 3 (one tiny exercise) only. Skip new material entirely. Showing up beats covering ground.
- **Normal day (~60–80 min):** All 5 sessions as above.
- **High-energy day (2+ hrs available):** Do the normal day, then either (a) pull in tomorrow's concept early, or (b) spend the extra time purely inside the project — extending a feature, not learning something new. Don't cram multiple new concepts back-to-back; if you have energy, go deeper on one thing, not wider on many.

---

## 8. Python Crash Course (Targeted, Not Beginner)

For each: what to understand / what to skip / tiny exercise / recall question / project use.

| Topic | Understand | Skip | Tiny Exercise | Project Use |
|---|---|---|---|---|
| Functions/args/defaults | positional vs keyword args, default values, `*args`/`**kwargs` basics | deep functional-programming patterns | write a function validating a file extension | input validation helpers |
| Classes | `__init__`, instance attributes, methods | multiple inheritance, metaclasses | a `Document` class with filename/tags | data models before you add Pydantic/SQLAlchemy |
| Exceptions | try/except/finally, raising custom exceptions | exception chaining internals | a function that raises `ValueError` on bad input | FastAPI error handling |
| Type hints | basic types, `Optional`, `List[str]` | `Generic`/`TypeVar` deep dives | annotate a function's signature | Pydantic models rely entirely on this |
| Virtual environments | why isolation matters, `venv` create/activate | `poetry`/`pipenv` internals | create and activate one, install a package | every project starts here |
| Packages/imports | modules vs packages, relative imports | packaging/publishing to PyPI | split code into 2 files, import between them | project folder structure |
| Comprehensions | list/dict comprehensions | nested comprehensions beyond 1 level | rewrite a for-loop as a comprehension | filtering search results |
| Generators | `yield`, why they save memory | generator internals/`send()` | write a generator reading file lines | reading large uploaded files |
| Decorators | what wraps what, why FastAPI uses them | writing decorators with arguments (until needed) | write a `@log_time` decorator | understanding `@app.get(...)` |
| Logging | `logging` module basics, log levels | log rotation/handlers config | log a message at INFO and ERROR level | tracking uploads/errors |
| Async/await | what `async def` changes, why FastAPI likes it | asyncio internals, event loop details | an async function that awaits `asyncio.sleep` | FastAPI route functions |
| pytest | test functions, `assert`, fixtures basics | plugins, parametrize edge cases (until needed) | write one passing, one failing test | testing your endpoints |

**Primary resource for the whole crash course:** the official Python docs tutorial sections for whatever's fuzzy (docs.python.org/3/tutorial) — read only the relevant section, not the whole tutorial.
**Backup:** Corey Schafer's Python OOP/decorators/generators YouTube videos (each is short and focused, matches your session length).

---

## 9. Software Fundamentals Path

Git → Linux/terminal → HTTP → REST → JSON → APIs → SQL → PostgreSQL → Authentication.

- **Git:** you already have exposure — the exit test is: clone, branch, commit, push, open a PR to your own repo, without looking anything up.
- **Linux/terminal:** just enough — navigating directories, editing `.env` files, running Docker commands. Not a full Linux course.
- **HTTP/REST/JSON:** exit test — explain a full request/response cycle for `POST /documents` including status codes.
- **SQL/PostgreSQL:** exit test is in Section 5, Week 2 checkpoint.
- **Authentication:** exit test is in Section 5, Week 3 checkpoint.

**Primary resource:** MDN Web Docs for HTTP/REST basics (developer.mozilla.org/en-US/docs/Web/HTTP). **For SQL:** PostgreSQL's own tutorial (postgresql.org/docs/current/tutorial.html), sections on SELECT/joins only.

---

## 10. FastAPI Path (Progressive)

1. Single hardcoded GET route → 2. Pydantic request/response models → 3. Path/query parameters → 4. Connecting a database → 5. `Depends()` for shared logic (like "get current user") → 6. File upload handling → 7. Exception handlers → 8. Auto docs (`/docs`) as your primary manual-testing tool throughout.

**Primary resource:** the official FastAPI tutorial (fastapi.tiangolo.com/tutorial) — it's already structured in small sections; work through it *in project order*, not front-to-back in one sitting.

---

## 11. Personal Knowledge API — Version-by-Version Evolution

- **v0:** Bare FastAPI app, one hardcoded GET route.
- **v1:** API + database — CRUD on `documents` table via Postgres.
- **v2:** Users/authentication — register/login, JWT, documents scoped to `user_id`.
- **v3:** File uploads — PDF/TXT/MD/CSV upload, stored on disk, metadata in DB.
- **v4:** Search/tags — keyword search across filename/tags/extracted text.
- **v5:** Tests/logging/error handling — pytest suite, structured logs, consistent error JSON.
- **v6:** Docker — Dockerfile + docker-compose (app + Postgres).
- **v7:** Deployment — live on a free-tier host, reachable by URL.

Each version should be a real git commit/tag — you should be able to check out `v3` and have a working (if incomplete) app.

---

## 12. Final Architecture

```
personal-knowledge-api/
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── config.py            # env vars / settings
│   ├── database.py          # DB session/engine setup
│   ├── models.py            # SQLAlchemy models (User, Document)
│   ├── schemas.py           # Pydantic request/response models
│   ├── auth.py               # password hashing, JWT create/verify
│   ├── routers/
│   │   ├── auth.py           # /register /login
│   │   ├── documents.py      # /documents CRUD + search
│   ├── services/
│   │   └── file_handling.py  # save file, extract text
│   └── dependencies.py       # get_current_user, get_db
├── tests/
│   └── test_documents.py
├── uploads/                  # stored files (gitignored)
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

**Why each piece exists:** `routers/` separates concerns by resource (REST convention); `schemas.py` vs `models.py` separates what the API exposes from what the DB stores (never leak password hashes back in a response); `dependencies.py` centralizes auth-checking so it's not repeated per-route; `services/` isolates file-handling logic so routes stay thin and testable.

**Auth flow:** client sends email/password to `/login` → server verifies hash → server returns signed JWT → client sends JWT in `Authorization: Bearer` header on future requests → `get_current_user` dependency decodes/verifies it on protected routes.

**Upload flow:** client sends multipart file to `/documents/upload` → FastAPI validates extension/size → file saved to disk (or object storage later) → text extracted where feasible → metadata row inserted, linked to `user_id`.

**Search flow:** client hits `/documents/search?q=...` → SQL query filters on filename/tags/extracted-text using `ILIKE` or Postgres full-text search → results scoped to the authenticated user.

---

## 13. Exercises (Progressive Difficulty)

1. Write a function validating a file extension against an allowed list.
2. Create a `Document` class with `to_dict()`.
3. Write a decorator that logs a function's execution time.
4. Write a generator that yields lines from a text file.
5. Create a FastAPI GET endpoint returning a static list.
6. Create a FastAPI POST endpoint validated by a Pydantic model.
7. Write a SQL query retrieving all documents for a given `user_id`, most recent first.
8. Add JWT-based auth to a previously-open endpoint.
9. Write a pytest test asserting a 401 on an unauthenticated request.
10. Write a pytest test asserting a successful file upload returns the correct metadata.
11. Dockerize the minimal FastAPI app (no DB yet).
12. Extend the Dockerfile/compose to include Postgres as a second service.

---

## 14. Debugging Challenges (Sample Categories)

Practice with deliberately broken code in each area — ask "why does this fail?" before looking at any fix:

- **Python:** a function raising `TypeError` because of a mutable default argument.
- **FastAPI:** a route returning a `422` because the Pydantic model doesn't match the request body.
- **SQL:** a query returning zero rows because of a type mismatch (comparing `id` as string vs int).
- **PostgreSQL/connection:** app fails to start because the DB connection string is wrong inside Docker (`localhost` vs the service name).
- **Auth:** a protected route returns `401` because the token isn't sent with the `Bearer` prefix.
- **Async:** a route hangs because a blocking call is used inside an `async def` without `await`.
- **Docker:** container exits immediately because the `CMD` is wrong or a port isn't exposed.

When you hit real bugs during the project (you will), treat them as free instances of this exercise.

---

## 15. Testing Strategy

- **What to test:** registration/login success and failure cases, protected-route access with/without a valid token, file upload success and rejected-file-type cases, search returning expected results, and that a user can't see another user's documents.
- **When:** write the test right after building each endpoint in Weeks 3–4, not all at once in Week 5 — Week 5 is for filling gaps and adding error-handling tests specifically.
- **Tooling:** `pytest` + FastAPI's `TestClient`; a separate test database (or SQLite in-memory for speed) so tests don't pollute real data.

---

## 16. Docker + Deployment (Only What You Need)

- **Dockerfile:** one stage, Python base image, install `requirements.txt`, copy app, run `uvicorn`.
- **docker-compose.yml:** two services — `app` and `db` (Postgres image), with the app depending on the DB and reading connection details from environment variables.
- **Secrets:** use a `.env` file (gitignored) with a `.env.example` committed for reference — never hardcode credentials.
- **Deployment:** pick **one** free-tier PaaS (Render, Railway, or Fly.io) that supports Docker Compose or a Dockerfile deploy directly — don't research all three, just pick one and follow its own quickstart.
- **Explicitly skipped:** Kubernetes, multi-stage optimization, CI/CD pipelines — none of these are needed to have a working, deployed Month-1 project.

---

## 17. Resource Library

| Topic | Primary Resource | Exact Section | Est. Time | Why |
|---|---|---|---|---|
| Python revision | Official Python Tutorial (docs.python.org/3/tutorial) | Classes, Errors/Exceptions, Modules | as-needed per concept | Authoritative, sectioned, free |
| Decorators/generators (backup) | Corey Schafer YouTube | "Decorators" and "Generators" videos | ~20-25 min each | Short, focused, matches session length |
| Git | Git official docs / "Git Basics" chapter of Pro Git (free online) | Ch. 2 (Basics), Ch. 3 (Branching) | ~1-2 sessions | Free, canonical, well-organized |
| HTTP/REST | MDN Web Docs | "HTTP overview", "HTTP response status codes" | ~2 sessions | Best free explanation of HTTP semantics |
| SQL/PostgreSQL | PostgreSQL official tutorial | Ch. 2-5 (queries, joins) | ~3-4 sessions | Matches the actual DB you're using |
| FastAPI | Official FastAPI Tutorial | Follow project order (Section 10 above) | ongoing through Weeks 1-4 | Written by the framework author, example-driven |
| SQLAlchemy | SQLAlchemy 2.0 ORM Quickstart (official docs) | "ORM Quick Start" only | ~2 sessions | Just enough to connect FastAPI ↔ Postgres |
| JWT/auth | FastAPI's own "Security" tutorial section | OAuth2 with Password and JWT chapter | ~2-3 sessions | Directly matches your stack, avoids generic JWT theory |
| pytest | FastAPI's own "Testing" tutorial section | TestClient examples | ~2 sessions | Framework-specific, not generic pytest theory |
| Docker | Docker's official "Get Started" guide | Part 1-3 only | ~2-3 sessions | Official, minimal, skips orchestration you don't need |

Avoid stacking multiple courses per topic — one primary source per row, used only for its relevant section.

---

## 18. Retention System

- **Daily recall (5 min):** before starting new material, write or say one sentence per concept learned in the last 2 days.
- **Weekly review (30–45 min):** at the end of each week, without notes: explain that week's checkpoint concept, then re-run that week's project version (`vN`) from a fresh terminal to confirm it still works.
- **Spaced revisits, built into the roadmap itself:**
  - Functions/classes: learned Week 1 → recalled Week 2 (used in DB models) → used in project every week after → debugged in Week 5.
  - SQL: learned Week 2 → recalled/extended Week 4 (search queries) → reviewed Week 6 (Docker DB connection).
  - Auth: learned Week 3 → used in every route from Week 4 onward → explained again in Week 6 deployment (env vars/secrets).
- The project itself is the primary spaced-repetition engine — you're not maintaining a separate flashcard system.

---

## 19. Weekly Checkpoints (Exit Criteria)

- **Week 1:** Create a new FastAPI app from scratch with a GET and POST route, unaided.
- **Week 2:** Create a table, write CRUD + JOIN queries, explain primary/foreign keys, connect Postgres to FastAPI.
- **Week 3:** Register, log in, get a token, access a protected route — and explain each step.
- **Week 4:** Upload each supported file type, tag it, retrieve it, find it via search.
- **Week 5:** `pytest` passes on core flows; bad requests return sensible errors, not stack traces.
- **Week 6:** A stranger can `docker compose up` your repo and hit your live-deployed API.

Do not advance past a checkpoint you can't pass without notes — go back and redo the recall step instead.

---

## 20. Final Capstone Checklist — "Month 1 Complete"

- [ ] Can create a Python backend project and structure it sensibly from an empty folder
- [ ] Can create and wire up FastAPI routes
- [ ] Can model data and write SQL against PostgreSQL
- [ ] Can validate requests with Pydantic
- [ ] Can implement and explain JWT authentication
- [ ] Can handle file uploads correctly
- [ ] Can implement basic keyword search
- [ ] Can write and run pytest tests for core flows
- [ ] Can debug a failure by reading an error, forming a hypothesis, and testing it
- [ ] Can add and read structured logs
- [ ] Can use Git for the full project history (branches, commits)
- [ ] Can Dockerize the application (app + Postgres)
- [ ] Can deploy it and share a working URL
- [ ] Can read unfamiliar documentation and solve a new problem independently

