"""
OG Image Converter — Pharmacie Charnal
Converts any image to 1200x630 Open Graph format.
Uses face detection (OpenCV) to avoid cropping heads.
Output: /images/Blog photos/OG generated/
"""

import streamlit as st
from PIL import Image
from pathlib import Path
import numpy as np
import cv2
import io

OG_WIDTH = 1200
OG_HEIGHT = 630
OG_RATIO = OG_WIDTH / OG_HEIGHT  # 1.904...
OUTPUT_DIR = Path(__file__).parent / "Blog photos" / "OG generated"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load face detector once
_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
_face_cascade = cv2.CascadeClassifier(_cascade_path)


def detect_faces(img: Image.Image) -> list[tuple[int, int, int, int]]:
    """Detect faces and return list of (x, y, w, h) bounding boxes."""
    arr = np.array(img)
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    faces = _face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) == 0:
        return []
    return [(int(x), int(y), int(w), int(h)) for x, y, w, h in faces]


def smart_crop_to_og(img: Image.Image) -> tuple[Image.Image, str]:
    """Crop image to 1.91:1 ratio centered on faces, then resize to 1200x630.
    Returns (cropped_image, method_used)."""
    w, h = img.size
    current_ratio = w / h

    if abs(current_ratio - OG_RATIO) < 0.01:
        return img.resize((OG_WIDTH, OG_HEIGHT), Image.LANCZOS), "exact ratio"

    faces = detect_faces(img)

    if current_ratio > OG_RATIO:
        # Image too wide — crop sides, center on faces horizontally
        new_w = int(h * OG_RATIO)
        if faces:
            # Center crop on the horizontal midpoint of all faces
            face_center_x = int(np.mean([x + fw // 2 for x, y, fw, fh in faces]))
            left = max(0, min(face_center_x - new_w // 2, w - new_w))
            method = f"face-aware horizontal ({len(faces)} visage(s))"
        else:
            left = (w - new_w) // 2
            method = "center horizontal"
        img = img.crop((left, 0, left + new_w, h))

    else:
        # Image too tall — crop top/bottom, protect faces vertically
        new_h = int(w / OG_RATIO)
        if faces:
            # Find the top of the highest face (with padding above for hair/head)
            face_top = min(y for x, y, fw, fh in faces)
            face_bottom = max(y + fh for x, y, fw, fh in faces)
            # Add 30% padding above topmost face for hair
            head_padding = int((face_bottom - face_top) * 0.3)
            face_top_padded = max(0, face_top - head_padding)

            # Center the crop window on the face region
            face_center_y = (face_top_padded + face_bottom) // 2
            top = max(0, min(face_center_y - new_h // 2, h - new_h))

            # Safety: ensure no face top (with padding) is cut off
            if top > face_top_padded:
                top = max(0, face_top_padded)
            # Ensure crop doesn't exceed image
            if top + new_h > h:
                top = h - new_h

            method = f"face-aware vertical ({len(faces)} visage(s))"
        else:
            # No faces: bias 40% from top (rule of thirds)
            top = int((h - new_h) * 0.4)
            method = "center vertical (pas de visage)"
        img = img.crop((0, top, w, top + new_h))

    return img.resize((OG_WIDTH, OG_HEIGHT), Image.LANCZOS), method


st.set_page_config(page_title="OG Image Converter", page_icon="🖼", layout="centered")

st.title("OG Image Converter")
st.caption("1200 x 630px — Open Graph pour LinkedIn, Facebook, Twitter")
st.caption("Detection automatique des visages pour eviter de couper les tetes")

uploaded = st.file_uploader(
    "Glisse une image ici",
    type=["png", "jpg", "jpeg", "webp"],
    accept_multiple_files=True,
)

if uploaded:
    for file in uploaded:
        img = Image.open(file).convert("RGB")
        og_img, method = smart_crop_to_og(img)

        stem = Path(file.name).stem
        out_name = f"og-{stem}.jpg"
        out_path = OUTPUT_DIR / out_name

        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption=f"Original ({img.size[0]}x{img.size[1]})", use_container_width=True)
        with col2:
            st.image(og_img, caption=f"OG (1200x630)", use_container_width=True)

        st.caption(f"Methode: {method}")

        # Save
        og_img.save(out_path, "JPEG", quality=90, optimize=True)
        file_size_kb = out_path.stat().st_size / 1024

        st.success(f"Sauvegarde: `OG generated/{out_name}` ({file_size_kb:.0f} KB)")

        # Download button
        buf = io.BytesIO()
        og_img.save(buf, "JPEG", quality=90, optimize=True)
        st.download_button(
            f"Telecharger {out_name}",
            data=buf.getvalue(),
            file_name=out_name,
            mime="image/jpeg",
        )

    st.divider()
    st.info(f"{len(uploaded)} image(s) convertie(s) dans `Blog photos/OG generated/`")
