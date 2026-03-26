# pdf2latex

A local-first CLI tool to convert PDF slides into structured text, review images interactively, and optionally generate LaTeX using AI.

---

## ✨ Features

- 📄 Extract text and images per slide
- 🧠 Structured output (JSON + readable text)
- 👁️ Interactive review UI (keyboard + mouse)
- ⚡ Fully local (AI optional)
- 🤖 Claude Code integration (optional)
- 📁 Batch processing (directories supported)
- 🔀 Merge multiple outputs

---

## 🧭 Repository Structure

```
pdf2latex/
├── pdf2latex.sh        # Main CLI entrypoint (handles all modes)
├── extract.py          # Extract text + images → slides.json
├── format.py           # Convert JSON → structured.txt + prompt.txt
├── review.py           # Interactive TUI for image selection
├── merge.py            # Merge multiple LaTeX outputs
│
├── templates/
│   └── prompt.txt      # Prompt template for AI generation
│
├── docs/
│   ├── SETUP.md        # Installation instructions
│   ├── USAGE.md        # CLI usage and workflows
│   └── CUSTOMIZATION.md# How to customize behavior
│
├── output/             # Generated outputs (auto-created)
│   └── <file_hash>/    # One folder per processed PDF
│       ├── images/     # Extracted images
│       ├── slides.json # Structured data (editable)
│       ├── structured.txt # Human-readable version
│       ├── prompt.txt  # AI-ready input
│       └── output.tex  # Final LaTeX (if AI used)
│
├── requirements.txt    # pip fallback dependencies
└── pyproject.toml      # uv support (optional)
```

---

## 🚀 Quick Start

```bash
git clone <repo>
cd pdf2latex
chmod +x pdf2latex.sh

./pdf2latex.sh slides.pdf
```

---

## 👁️ Review Images (Important Step)

```bash
./pdf2latex.sh review output/<lecture_dir>
```

---

## 📖 Documentation

- 👉 [Setup Guide](docs/SETUP.md)
- 👉 [Usage Guide](docs/USAGE.md)
- 👉 [Customization](docs/CUSTOMIZATION.md)

---

## 🧠 Philosophy

- Local-first
- Human-in-the-loop
- AI is optional, not required

---

## 🛠 Roadmap

- [ ] Image deduplication
- [ ] Parallel processing
- [ ] Plugin system (Claude / local LLMs)
- [ ] Markdown export
- [ ] PDF → compiled LaTeX directly
