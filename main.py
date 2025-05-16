from PIL import Image, ImageOps
import os

import pikepdf

# A4 size in pixels at 300 DPI
A4_PX = (2480, 3508)

# Get base directory and paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(BASE_DIR, "images")
output_pdf_path = os.path.join(BASE_DIR, "generated", "output.pdf")

# Ensure output directory exists
os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

# Get all PNG images sorted
image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(".png")])

pdf_pages = []

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    with Image.open(image_path) as img:
        img = img.convert("RGB")

        # Resize and crop to fill full A4 page
        img = ImageOps.fit(img, A4_PX, Image.Resampling.LANCZOS)

        pdf_pages.append(img)

# Save to PDF
if pdf_pages:
    pdf_pages[0].save(
        output_pdf_path,
        save_all=True,
        append_images=pdf_pages[1:],
        resolution=300,
        quality=100,
    )
    print(f"✅ Full-page high-quality PDF created: {output_pdf_path}")
else:
    print("❌ No PNG images found in the folder.")
