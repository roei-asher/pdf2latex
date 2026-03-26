# Setup

## Requirements

- Python 3.9+
- Bash (Linux / macOS / WSL on Windows)

---

## Option 1 — Using uv (Recommended)

Install uv:

https://github.com/astral-sh/uv

Then:

```bash
uv venv
uv pip install pymupdf textual pillow
```

---

## Option 2 — Using pip

```bash
pip install pymupdf textual pillow
```

---

## Make Script Executable

```bash
chmod +x pdf2latex.sh
```

---

## Optional: Claude CLI

Install Claude Code CLI if you want AI → LaTeX:

https://docs.anthropic.com

Verify installation:

```bash
claude --version
```
