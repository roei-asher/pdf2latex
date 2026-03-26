import fitz
import json
import os
import sys

pdf_path = sys.argv[1]
outdir = sys.argv[2]

doc = fitz.open(pdf_path)

img_dir = os.path.join(outdir, "images")
os.makedirs(img_dir, exist_ok=True)

slides = []

for i, page in enumerate(doc):
    text = page.get_text()
    images = []

    for j, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base = doc.extract_image(xref)
        ext = base["ext"]

        path = os.path.join(img_dir, f"page{i}_img{j}.{ext}")
        with open(path, "wb") as f:
            f.write(base["image"])

        images.append(path)

    slides.append({"slide": i, "text": text, "images": images})

with open(os.path.join(outdir, "slides.json"), "w") as f:
    json.dump(slides, f, indent=2)
