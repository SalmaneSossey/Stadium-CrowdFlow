# Stadium CrowdFlow

Stadium CrowdFlow is a Smart City prototype that **predicts congestion around a stadium (by time + zone)** and provides **actionable operational recommendations** (routes, gates, buses, staff) for match days — with a strong Morocco 2030 / large-events narrative.

---

## MVP (What we must deliver)
1) **Congestion risk prediction** by **time + zone**  
2) **Dashboard**: heatmap + timeline + risk indicator  
3) **Recommendations**: concrete actions triggered by predicted risk  
4) **Evaluation**: basic metric (or simulation “before/after” impact)

**One-line MVP:**  
A dashboard that predicts stadium-area congestion and recommends actions to reduce crowd/traffic risk.

---

## Repo structure
```text
Stadium-CrowdFlow/
  README.md
  CONTRIBUTING.md
  LICENSE
  .gitignore
  .env.example
  docker-compose.yml
  docs/
    TASKS.md
    DECISIONS.md
    pitch/
    screenshots/
  data/
    raw/          # ignored (no big data in git)
    processed/    # ignored
    sample/       # small committed examples (CSV/JSON)
  backend/
    app/
      main.py
      api/
      services/
      models/
    tests/
    pyproject.toml
  frontend/
    .keep
  notebooks/
    .keep
  scripts/
    .keep
``` 

---

## Team onboarding (Read first)
### 1) Clone
```bash
git clone https://github.com/SalmaneSossey/Stadium-CrowdFlow.git
cd Stadium-CrowdFlow
```
### 2) Environement variables
Never commit secrets.

Copy and edit locally:

```
cp .env.example .env

```

### 3) Start Working (branch rule)
Never push directly to `main`. Create a branch:
```
git checkout -b feat/<topic>
# examples:
# feat/dashboard
# feat/model-baseline
# feat/api
# feat/pitch

```

### Workflow rules (Hackathon-safe, conflict-free)
### Pull Requests (PRs)

Open a PR to main

Keep PRs small

Add a short description

Add a screenshot for UI changes (if relevant)

### Commit messages (recommended)

`feat`: ... new feature

`fix`: ... bug fix

`chore`: ... repo / tooling / cleanup

`docs`: ... documentation

### Data & secrets policy (Important)
 
Allowed in repo:

Small sample files in `data/sample/` (tiny CSV/JSON)

Documentation of data sources (in `docs/`)

  Not allowed in repo:

`.env` files, API keys, tokens

Large datasets
(Folders `data/raw/` and `data/processed/` are intentionally ignored)


### Tasks & ownership

See:

`docs/TASKS.md` (task board + owners)

`docs/DECISIONS.md` (final decisions log)

### How to run (to be finalized)

-- We will add one-command run (Docker) once the stack is locked.--

Planned options:

Backend: FastAPI/Flask

Frontend: Streamlit or Next.js

### Demo checklist (final presentation)

Live dashboard showing: heatmap + timeline + predicted peaks

Recommendations panel with 3–5 concrete actions

Short evaluation: accuracy metric or simulated congestion reduction

Backup: screenshots/video in docs/screenshots/ (optional)

### Contributing

Read CONTRIBUTING.md before your first PR.

### License

TBD (MIT recommended for hackathon projects).
