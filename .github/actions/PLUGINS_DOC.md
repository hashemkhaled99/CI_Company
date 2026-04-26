**.github/actions — Plugin Folder Documentation**

This document describes the custom GitHub Actions plugins in the repository, what each plugin currently does, required configuration and dependencies, and a step-by-step checklist to reach a successful CI run ("100% success" = all actions complete without error and coverage/lint gates satisfied).

**Quick Links**
- **CI workflow**: [.github/workflows/ci.yml](.github/workflows/ci.yml)
- **Plugin folder**: [.github/actions](.github/actions)

**Folder Structure**
- `.github/actions/`
  - `lint-python/` — [.github/actions/lint-python/action.yml](.github/actions/lint-python/action.yml)
  - `lint-go/` — [.github/actions/lint-go/action.yml](.github/actions/lint-go/action.yml)
  - `lint-react/` — [.github/actions/lint-react/action.yml](.github/actions/lint-react/action.yml)
  - `lint-sql/` — [.github/actions/lint-sql/action.yml](.github/actions/lint-sql/action.yml)
  - `test-python/` — [.github/actions/test-python/action.yml](.github/actions/test-python/action.yml)
  - `test-go/` — [.github/actions/test-go/action.yml](.github/actions/test-go/action.yml)
  - `test-react/` — [.github/actions/test-react/action.yml](.github/actions/test-react/action.yml)

**Mapping to CI jobs**
See job names and wiring in the CI workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml).
- `lint-python` → uses `.github/actions/lint-python`
- `test-python` → uses `.github/actions/test-python`
- `lint-go` → uses `.github/actions/lint-go`
- `test-go` → uses `.github/actions/test-go`
- `lint-react` → uses `.github/actions/lint-react`
- `test-react` → uses `.github/actions/test-react`
- `lint-sql` → uses `.github/actions/lint-sql`

**Important note on naming / current behavior**
- Some plugin folders are currently named `lint-*` but actually run tests (for example, `.github/actions/lint-python/action.yml` runs `pytest`). The documentation below reflects the *actual* behavior as configured in the repository and then provides a recommended alignment (rename or rewrite) where appropriate.

**Per-plugin details & requirements**

- **Lint / Test: Python** — [.github/actions/lint-python/action.yml](.github/actions/lint-python/action.yml)
  - Purpose (current): Runs `pytest` with a coverage gate (currently configured at 80%).
  - Key steps (taken from action):
    ```bash
    pip install pytest pytest-cov
    pytest trying/ --cov=trying --cov-fail-under=80 --cov-report=term-missing
    ```
  - Requirements to succeed (100% success checklist):
    - `trying/` must contain tests and be importable as a package (include `__init__.py` if needed).
    - `requirements.txt` or other dependency manifest must list test dependencies, or tests must not require external deps.
    - Python version compatibility: action uses `setup-python@v5` with `python-version: '3.11'`.
    - Coverage: Ensure measured coverage for `trying` ≥ 80% (current action gate). To guarantee success, add/expand tests to exercise code paths.
  - Troubleshooting tips:
    - Run locally: `pytest trying/ --cov=trying --cov-report=term-missing`
    - Fix import errors by adjusting `PYTHONPATH` or package layout.
  - Recommendation: rename this plugin to `test-python` or change its behavior to a linter (Ruff) and create a separate `test-python` action for tests (this repo already has `.github/actions/test-python`).

- **Test: Python (canonical)** — [.github/actions/test-python/action.yml](.github/actions/test-python/action.yml)
  - Purpose: Runs `pytest` with a 40% coverage gate.
  - Key steps:
    ```bash
    pip install pytest pytest-cov
    pytest trying/ --cov=trying --cov-fail-under=40 --cov-report=term-missing
    ```
  - Requirements to succeed:
    - Same as above but with coverage threshold ≥ 40%.
    - Make sure CI installs dependencies before running tests (either `pip install -r requirements.txt` or the action must include installation).
  - Local commands to validate:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest trying/ --cov=trying --cov-fail-under=40 --cov-report=term-missing
    ```

- **Lint / Test: Go** — [.github/actions/lint-go/action.yml](.github/actions/lint-go/action.yml)
  - Purpose (current): Runs Go tests and enforces an 80% coverage gate (note: folder is named `lint-go` but currently runs tests).
  - Action steps (observed): sets up Go `1.26.1` and runs:
    ```bash
    go test -v -coverprofile=coverage.out ./...
    go tool cover -func=coverage.out > coverage_report.txt
    # parse coverage and fail if < 80
    ```
  - Requirements to succeed:
    - Go toolchain installed (action uses `actions/setup-go@v5` with `go-version: '1.26.1'`). Locally ensure `go` >= required version.
    - `go.mod` and `go.sum` present and module-aware code. Run `go mod download` prior to tests if dependencies missing.
    - Tests present for packages under repository so coverage ≥ 80%.
  - Recommendation: If you intend a linter step, introduce `golangci-lint` in a proper `lint-go` action and move tests into `.github/actions/test-go` (which already exists in this repo).

- **Test: Go (canonical)** — [.github/actions/test-go/action.yml](.github/actions/test-go/action.yml)
  - Purpose: Runs Go tests with Race Detector and a 40% coverage gate.
  - Key steps:
    ```bash
    go test -v -race -coverprofile=coverage.out -covermode=atomic ./...
    go tool cover -func=coverage.out > coverage_report.txt
    # parse coverage and fail if < 40
    ```
  - Requirements to succeed:
    - Same as the lint-go requirements, but threshold is 40%.
    - Race detector (`-race`) requires cgo on some platforms; `ubuntu-latest` supports it. For reproducible runs use `ubuntu-latest` as in CI.
  - Local run:
    ```bash
    cd trying
    go test -v -race -coverprofile=coverage.out -covermode=atomic ./...
    go tool cover -func=coverage.out
    ```

- **Lint React (Biome)** — [.github/actions/lint-react/action.yml](.github/actions/lint-react/action.yml)
  - Purpose: Run Biome (JS/TS linter) in CI. Uses `biomejs/setup-biome@v2` and runs `biome ci .`.
  - Requirements to succeed:
    - `biome.json` present in repository root (this repo contains `biome.json`).
    - Node toolchain not strictly required for Biome CLI (depends on setup), but if using JS tooling also ensure `package.json` and `node` are correct.
    - `biome ci .` must exit with code 0 (no lints failing under CI rules).
  - Local command:
    ```bash
    npx biome ci .
    # or if biome installed globally
    biome ci .
    ```

- **Test React (Vitest)** — [.github/actions/test-react/action.yml](.github/actions/test-react/action.yml)
  - Purpose: Run `vitest` with a 40% coverage gate.
  - Steps used by action:
    ```bash
    npm ci
    npx vitest run --coverage.enabled --coverage.thresholds.lines=40
    ```
  - Requirements to succeed:
    - `package.json` with dev dependencies (vitest) and test files present.
    - Coverage reporter configured (vitest uses `coverage`/`c8` internally); ensure test environment produces coverage reports.
  - Local run:
    ```bash
    npm ci
    npx vitest run --coverage
    ```

- **Lint SQL (SQLFluff)** — [.github/actions/lint-sql/action.yml](.github/actions/lint-sql/action.yml)
  - Purpose: Run `sqlfluff` with dialect `postgres`.
  - Key steps:
    ```bash
    pip install sqlfluff
    sqlfluff lint . --dialect postgres
    ```
  - Requirements to succeed:
    - SQL files present and written for the configured dialect.
    - Optional `.sqlfluff` config to enforce rules and exclude directories.
  - Local run:
    ```bash
    pip install sqlfluff
    sqlfluff lint path/to/sql
    ```

**Cross-cutting CI requirements & permissions**
- The CI workflow (`.github/workflows/ci.yml`) performs `actions/checkout@v4` in jobs; some jobs (secret scanning/gitleaks) require `fetch-depth: 0` to scan full history.
- The PR sticky-comment step uses `marocchino/sticky-pull-request-comment@v2` and requires `permissions: pull-requests: write` for the `report` job.
- `concurrency` is configured in the workflow to cancel in-progress runs for the same PR to save resources.

**What "100% success" means (practical checklist)**
1. All required config files exist and are correct:
   - `pyproject.toml` / `requirements.txt` / optional `pytest.ini` for Python
   - `biome.json` for Biome
   - `package.json` + dev deps for React tests (Vitest)
   - `go.mod` for Go
   - `.sqlfluff` if you have custom SQLFluff rules
2. Tests exist and exercise code paths to meet coverage gates configured in actions (40% for many test jobs; some older actions still gate at 80% — see per-action configuration above).
3. CI dependencies are installed successfully in jobs (use `pip`, `npm ci`, `go mod download` where applicable).
4. Lint rules are satisfied (or configured to `warn` instead of `error` if desired).
5. Jobs are running on `ubuntu-latest` (as the workflow expects), and any platform-sensitive flags (like Go `-race`) are supported.
6. Required GitHub permissions and tokens are present (the default `GITHUB_TOKEN` is used for most actions; the report step requires `pull-requests: write`).

**Local developer quick-check commands**
- Python unit tests & coverage (40%):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest trying/ --cov=trying --cov-fail-under=40 --cov-report=term-missing
```
- Go tests (race + 40%):
```bash
go version
cd trying
go test -v -race -coverprofile=coverage.out -covermode=atomic ./...
go tool cover -func=coverage.out
```
- React tests (Vitest + coverage):
```bash
node -v
npm ci
npx vitest run --coverage
npx biome ci .
```
- SQLFluff lint:
```bash
pip install sqlfluff
sqlfluff lint path/to/sql
```

**Recommendations & best practices**
- Align folder names and action responsibilities: make `lint-*` actions actually run linters (`ruff`, `golangci-lint`, `biome`, `sqlfluff`) and `test-*` actions run tests. This reduces cognitive load and avoids duplicate testing.
- Move coverage thresholds into the corresponding `test-*` action only; keep `lint-*` actions strictly for linting.
- Add explicit `install dependencies` steps where missing (for example, the `lint-python` action currently does not `pip install -r requirements.txt` — ensure tests/lint can import project code).
- Add caching for package managers (`actions/cache` or built-in caching in `setup-node`, `setup-python`, `setup-go`) to speed CI.
- Add `go mod download` before `go test` to ensure modules are available.
- Prefer running linters in `check` mode on CI and optionally `--fix` in dev flows.

**Troubleshooting common failures**
- Import errors in Python tests: ensure `PYTHONPATH` or package layout is correct. If `trying` is a package, ensure it contains `__init__.py` or adjust `pytest` invocation.
- Coverage below threshold: add unit tests that cover missing branches/functions and focus on critical modules; consider temporarily reducing the gate while you add tests.
- Biome/Node/JS failures: ensure `node` version matches `engines` in `package.json`; run `npm ci` locally to reproduce.
- Go `-race` failures or unsupported platforms: run tests without `-race` locally to reproduce, but keep `-race` in CI for safety.

**Next actions I can take for you**
- Generate aligned, corrected `action.yml` templates for each plugin (separate lint vs test responsibilities).
- Open a PR with the new `PLUGINS_DOC.md` and suggested `action.yml` changes.
- Add missing dependency install steps or caching improvements.

---

Documentation created at: [.github/actions/PLUGINS_DOC.md](.github/actions/PLUGINS_DOC.md)
CI workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml)

If you'd like, I can now: generate corrected `action.yml` templates for each plugin, or open a PR with the changes. Which would you prefer?