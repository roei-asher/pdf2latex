import os
import sys

base_dir = sys.argv[1]

files = []

for root, _, filenames in os.walk(base_dir):
    for f in filenames:
        if f == "output.tex":
            files.append(os.path.join(root, f))

files.sort()

with open("merged.tex", "w") as out:
    for file in files:
        with open(file) as f:
            out.write(f.read())
            out.write("\n\n")

print("✅ merged.tex created")
