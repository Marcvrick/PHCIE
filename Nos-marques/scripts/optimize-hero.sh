#!/usr/bin/env bash
# Optimize a hero background photo for the Pharmacie Charnal brand pages.
#
# Pipeline:
#   1. Resize to max 2400 wide (preserve aspect ratio) with sips
#   2. Strip metadata (EXIF, ICC profiles)
#   3. Re-encode as progressive JPEG with cjpeg (libjpeg-turbo) at quality 82
#   4. Output: Nos-marques/logos/{BrandName}-hero.jpg
#
# Usage:
#   ./optimize-hero.sh INPUT_FILE SLUG [BRAND_NAME]
#
# SLUG is the short identifier (lowercase, hyphenated). The script maps it to
# the canonical Brand-Name format used in filenames. If you pass BRAND_NAME
# explicitly as a third argument, that override is used instead.
#
# Examples:
#   ./optimize-hero.sh ~/Downloads/Aragan-hd.jpg aragan          → Aragan-hero.jpg
#   ./optimize-hero.sh ~/Downloads/Nuxe.png nuxe                  → Nuxe-hero.jpg
#   ./optimize-hero.sh ~/Downloads/photo.png la-roche-posay       → La-Roche-Posay-hero.jpg
#   ./optimize-hero.sh ~/Downloads/photo.png sid-nutrition        → SID-Nutrition-hero.jpg
#
# Target sizes:
#   - 2400×~1029 px (21:9)  → ~180-280 KB
#   - JPEG progressive q=82 (sweet spot quality/weight)

set -euo pipefail

INPUT="${1:?Usage: $0 INPUT_FILE SLUG [BRAND_NAME]}"
SLUG="${2:?Usage: $0 INPUT_FILE SLUG [BRAND_NAME]}"
BRAND_OVERRIDE="${3:-}"

# Map slug → BrandName (used in filename). Override with 3rd arg if needed.
slug_to_brand() {
    case "$1" in
        bioderma)        echo "Bioderma" ;;
        biocanina)       echo "Biocanina" ;;
        biogaran)        echo "Biogaran" ;;
        bion3)           echo "Bion-3" ;;
        boiron)          echo "Boiron" ;;
        klorane)         echo "Klorane" ;;
        la-roche-posay)  echo "La-Roche-Posay" ;;
        larosee)         echo "La-Rosee" ;;
        avene)           echo "Avene" ;;
        nuxe)            echo "Nuxe" ;;
        mustela)         echo "Mustela" ;;
        natform)         echo "NatForm" ;;
        pileje)          echo "PiLeJe" ;;
        aragan)          echo "Aragan" ;;
        sid-nutrition|sid) echo "SID-Nutrition" ;;
        *)
            # Default fallback: capitalize first letter
            echo "$(echo "${1:0:1}" | tr '[:lower:]' '[:upper:]')${1:1}"
            ;;
    esac
}

if [[ -n "$BRAND_OVERRIDE" ]]; then
    BRAND_NAME="$BRAND_OVERRIDE"
else
    BRAND_NAME=$(slug_to_brand "$SLUG")
fi

WEBSITE_DIR="/Users/mc/Library/Mobile Documents/com~apple~CloudDocs/MarcOS/Pharma/Pharma online/website-pharmacie-charnal"
OUTPUT="$WEBSITE_DIR/Nos-marques/logos/$BRAND_NAME-hero.jpg"
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
echo "→ Brand name resolved: $BRAND_NAME"

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
