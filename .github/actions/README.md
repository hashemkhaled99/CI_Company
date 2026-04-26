# GitHub Actions: Plugin Folder

This folder contains small, reusable composite actions used by the repository CI.

Paths
- `.github/actions/lint-python` — Ruff-based Python linter
- `.github/actions/test-python` — Pytest with 40% coverage gate
- `.github/actions/lint-go` — golangci-lint
- `.github/actions/test-go` — `go test` with `-race` and 40% coverage gate
- `.github/actions/lint-react` — Biome linter for JS/TS
- `.github/actions/test-react` — Vitest with 40% coverage gate
- `.github/actions/lint-sql` — SQLFluff

Quick start
- Run the same checks locally to reproduce CI failures.

Python (tests):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest pytest-cov
pytest trying/ --cov=trying --cov-fail-under=40 --cov-report=term-missing
```

Python (linter - ruff):
```bash
pip install ruff
ruff check .
```

Go (tests):
```bash
cd trying
go mod download
go test -v -race -coverprofile=coverage.out -covermode=atomic ./...
go tool cover -func=coverage.out
```

Go (linter):
```bash
# uses golangci-lint-action in CI, locally:
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s latest
golangci-lint run ./...
```

React (tests):
```bash
npm ci
npx vitest run --coverage
```

SQL Lint:
```bash
pip install sqlfluff
sqlfluff lint . --dialect postgres
```

Contact
If you want me to open a PR with these changes, I will attempt to create a branch and push it to the remote and open a PR automatically (if the repository has a configured remote and you have `gh` CLI configured). If that fails, I'll provide the git commands to run locally.
