# 🖼️ Image to PDF Generator

Convert a folder of scanned `.png` images into a **single, high-quality PDF** formatted to A4 pages.

---

## 📌 Features

- ✅ Converts `.png` images to a multi-page PDF
- ✅ A4 page size (300 DPI) – print ready
- ✅ Maintains image quality
- ✅ Fills the entire PDF page (no white borders)
- ✅ Automatically sorts images by filename
- ✅ Works offline

---

## 📁 Folder Structure

```
Image-PDF-Generator/
│
├── images/             # Place all your .png images here
├── generated/          # Output PDF will be saved here
├── main.py             # Main script
└── README.md           # Project readme
````

---

## 🛠️ Requirements

- Python 3.8+
- Pillow (Python Imaging Library)

### 🔧 Install Dependencies

```bash
pip install pillow
````

---

## 🚀 How to Use

1. Clone or download this repository.
2. Put your `.png` images inside the `images/` folder.
3. Run the script:

```bash
python main.py
```

4. Your generated PDF will be saved at:

```
generated/output.pdf
```

---

## 📐 A4 Page Fit

This script uses `ImageOps.fit()` to **crop and scale** your images to fully fill each A4-sized PDF page (2480×3508 pixels at 300 DPI).

* No white borders
* Best for scanned documents or full-page graphics

---

## 📷 Image Format

* Only `.png` images are supported
* Images are sorted alphabetically (e.g., `page1.png`, `page2.png`, etc.)

---

## 📂 Example Use Cases

* Scanned documents to single PDF
* Form submissions
* Portfolio scans
* Offline print-ready conversions

---

## ⚡ Optional: Compress PDF Size

If your final PDF is too large, you can compress it using Ghostscript:

### Install Ghostscript:

* [Download for Windows](https://ghostscript.com/download/gsdnld.html)

### Run This Command (PowerShell):

```powershell
gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 `
  -dPDFSETTINGS=/ebook `
  -dNOPAUSE -dQUIET -dBATCH `
  -sOutputFile=generated\output_compressed.pdf `
  generated\output.pdf
```

| Setting     | Description                    |
| ----------- | ------------------------------ |
| `/screen`   | Lowest quality & smallest size |
| `/ebook`    | Medium quality & size          |
| `/prepress` | Highest quality                |

---

## ✍️ Author

**Mahamudul Hasan**
🌐 [Portfolio](https://mahamudul.codejet.dev)   ·   💼 [LinkedIn](https://www.linkedin.com/in/mahamudul-hasan-developer/)   ·   💻 [GitHub](https://github.com/Mahamudul-Dev)

---

## 📜 License

MIT License – free for personal and commercial use.

