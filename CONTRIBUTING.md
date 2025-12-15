# Contributing guide

## Workflow
1) Create a branch: `feat/<topic>` (no direct pushes to `main`)
2) Commit with clear messages: `feat:`, `fix:`, `chore:`, `docs:`
3) Open a Pull Request (PR) to `main`
4) At least one teammate reviews before merge

## Branch naming
- `feat/dashboard`
- `feat/api`
- `feat/model-baseline`
- `feat/pitch`

## Data & secrets
- Never commit `.env` or API keys/tokens
- Do not commit large datasets
- Only small examples go in `data/sample/` (CSV/JSON)

## Folder ownership (suggested)
- `backend/`  -> API + services
- `frontend/` -> dashboard UI
- `docs/`     -> pitch + documentation
- `models/` or `backend/app/models/` -> ML code
