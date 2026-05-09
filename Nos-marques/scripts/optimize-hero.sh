#!/usr/bin/env bash
# Optimize a hero background photo for the Pharmacie Charnal brand pages.
#
# Pipeline:
#   1. Resize to max 2400 wide (preserve aspect ratio) with sips
#   2. Strip metadata (EXIF, ICC profiles)
#   3. Re-encode as progressive JPEG with cjpeg (libjpeg-turbo) at quality 82
#   4. Output: Nos-marques/logos/{slug}-hero-bg.jpg
#
# Usage:
#   ./optimize-hero.sh INPUT_FILE SLUG
#
# Examples:
#   ./optimize-hero.sh ~/Downloads/Aragan-hd.jpg aragan
#   ./optimize-hero.sh ~/Downloads/Nuxe.png nuxe
#
# Target sizes:
#   - 2400×~1029 px (21:9)  → ~180-280 KB
#   - JPEG progressive q=82 (sweet spot quality/weight)

set -euo pipefail

INPUT="${1:?Usage: $0 INPUT_FILE SLUG}"
SLUG="${2:?Usage: $0 INPUT_FILE SLUG}"

WEBSITE_DIR="/Users/mc/Library/Mobile Documents/com~apple~CloudDocs/MarcOS/Pharma/Pharma online/website-pharmacie-charnal"
OUTPUT="$WEBSITE_DIR/Nos-marques/logos/$SLUG-hero-bg.jpg"
TMPDIR="/tmp/claude/hero-opt-$$"
mkdir -p "$TMPDIR"
trap 'rm -rf "$TMPDIR"' EXIT

if [[ ! -f "$INPUT" ]]; then
    echo "ERROR: input file not found: $INPUT" >&2
    exit 1
fi

# 0. Source info
SRC_DIMS=$(sips -g pixelWidth -g pixelHeight "$INPUT" 2>/dev/null | awk '/pixel/{print $2}' | paste -sd "x" -)
SRC_SIZE=$(stat -f%z "$INPUT")
echo "Source: $INPUT — ${SRC_DIMS}, $((SRC_SIZE / 1024)) KB"

# 1. Resize to max 2400 wide if larger
WIDTH=$(sips -g pixelWidth "$INPUT" 2>/dev/null | awk '/pixelWidth/{print $2}')
if [[ "$WIDTH" -gt 2400 ]]; then
    echo "→ Resizing to 2400 wide…"
    sips --resampleWidth 2400 -s format jpeg -s formatOptions 100 "$INPUT" --out "$TMPDIR/resized.jpg" >/dev/null
else
    echo "→ Source already ≤ 2400 wide ($WIDTH), keeping as-is for re-encoding"
    sips -s format jpeg -s formatOptions 100 "$INPUT" --out "$TMPDIR/resized.jpg" >/dev/null
fi

# 2. Decode → strip metadata → re-encode as progressive JPEG q=82
echo "→ Re-encoding as progressive JPEG q=82…"
djpeg "$TMPDIR/resized.jpg" 2>/dev/null \
    | cjpeg -quality 82 -progressive -optimize -outfile "$OUTPUT" 2>/dev/null

# 3. Report
OUT_DIMS=$(sips -g pixelWidth -g pixelHeight "$OUTPUT" 2>/dev/null | awk '/pixel/{print $2}' | paste -sd "x" -)
OUT_SIZE=$(stat -f%z "$OUTPUT")
SAVED=$((SRC_SIZE - OUT_SIZE))
echo
echo "✅ Output: $OUTPUT"
echo "   Dimensions: $OUT_DIMS"
echo "   Size: $((OUT_SIZE / 1024)) KB"
if [[ $SAVED -gt 0 ]]; then
    echo "   Saved: $((SAVED / 1024)) KB ($(( (SAVED * 100) / SRC_SIZE ))% smaller)"
fi
