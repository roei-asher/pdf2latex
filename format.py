import json
import sys
import os

outdir = sys.argv[1]

with open(os.path.join(outdir, "slides.json")) as f:
    slides = json.load(f)

lines = []

for slide in slides:
    lines.append(f"=== SLIDE {slide['slide']} ===")
    lines.append("TEXT:")
    lines.append(slide["text"].strip())
    lines.append("")
    lines.append("IMAGES:")

    for img in slide["images"]:
        lines.append(f"[IMG] {img}")

    lines.append("\n")

structured_path = os.path.join(outdir, "structured.txt")

with open(structured_path, "w") as f:
    f.write("\n".join(lines))

# also create prompt
with open("templates/prompt.txt") as f:
    template = f.read()

with open(os.path.join(outdir, "prompt.txt"), "w") as f:
    f.write(template + "\n\n" + "\n".join(lines))
