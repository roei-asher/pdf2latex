# Customization

## Prompt Template

Edit:

templates/prompt.txt

You can control:

- LaTeX structure
- verbosity
- formatting style

---

## Image Extraction

Modify:

extract.py

Ideas:

- skip small images
- filter duplicates
- convert formats (PNG → JPG)

---

## Output Formatting

Modify:

format.py

Options:

- change structured.txt format
- export Markdown instead
- add metadata

---

## Review UI

Modify:

review.py

Possible upgrades:

- fullscreen image preview
- annotations
- image reordering

---

## Add New CLI Modes

Modify:

pdf2latex.sh

Example:

```bash
pdf2latex stats file.pdf
pdf2latex export-md file.pdf
```

---

## Disable Images Entirely

In extract.py:

```python
images = []
```

---

## Advanced Ideas

- integrate local LLM (llama.cpp)
- build lightweight web UI
- auto compile LaTeX → PDF
- caching and deduplication
