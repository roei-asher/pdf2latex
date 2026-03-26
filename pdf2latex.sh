#!/usr/bin/env bash

INPUT="$1"
MODE="${2:-full}" # full | no-ai | extract-only

run_python() {
  if command -v uv &>/dev/null; then
    uv run "$@"
  else
    python3 "$@"
  fi
}

# -------- REVIEW MODE --------
if [ "$INPUT" = "review" ]; then
  TARGET="$2"

  if [ -z "$TARGET" ]; then
    echo "❌ Usage: pdf2latex review <output_dir>"
    exit 1
  fi

  run_python review.py "$TARGET"
  exit 0
fi

hash_path() {
  echo "$1" | md5sum | cut -c1-6
}

process_pdf() {
  PDF="$1"

  BASENAME=$(basename "$PDF" .pdf)
  HASH=$(hash_path "$PDF")
  OUTDIR="output/${BASENAME}_${HASH}"

  echo "== Processing: $PDF =="
  mkdir -p "$OUTDIR"

  # Skip if already done
  if [ -f "$OUTDIR/structured.txt" ]; then
    echo "⏭️ Skipping (already processed)"
    return
  fi

  run_python extract.py "$PDF" "$OUTDIR"
  run_python format.py "$OUTDIR"

  if [ "$MODE" != "no-ai" ] && command -v claude &>/dev/null; then
    echo "== Running Claude =="
    claude <"$OUTDIR/prompt.txt" >"$OUTDIR/output.tex" || {
      echo "⚠️ Claude failed"
    }
  fi

  echo "✅ Done → $OUTDIR"
  echo ""
}

export -f process_pdf
export -f run_python
export -f hash_path

# -------- FILE --------
if [ -f "$INPUT" ]; then
  process_pdf "$INPUT"

# -------- DIRECTORY --------
elif [ -d "$INPUT" ]; then
  find "$INPUT" -type f -name "*.pdf" | while read -r pdf; do
    process_pdf "$pdf" || echo "⚠️ Failed: $pdf"
  done

else
  echo "❌ Invalid input"
  exit 1
fi
