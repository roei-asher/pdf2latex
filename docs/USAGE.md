# Usage

## Single PDF

```bash
./pdf2latex.sh file.pdf
```

---

## Directory (Recursive)

```bash
./pdf2latex.sh lectures/
```

---

## No AI Mode (Recommended First Pass)

```bash
./pdf2latex.sh file.pdf no-ai
```

---

## Review Mode (Core Feature)

```bash
./pdf2latex.sh review output/<dir>
```

### Controls

| Key           | Action         |
| ------------- | -------------- |
| j / ↓         | next image     |
| k / ↑         | previous image |
| l / →         | next slide     |
| h / ←         | previous slide |
| Enter / Space | toggle image   |
| a             | select all     |
| d             | deselect all   |
| s             | save           |
| q             | quit           |

---

## Merge Outputs

```bash
python merge.py output/
```

---

## Recommended Workflow

```bash
# 1. Extract only
./pdf2latex.sh slides.pdf no-ai

# 2. Review and clean images
./pdf2latex.sh review output/<dir>

# 3. Generate LaTeX
./pdf2latex.sh slides.pdf
```
