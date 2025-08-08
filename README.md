# Dot-Art-Image-Renderer
Turn any image into elegant dot-style ASCII art using Python.
# 🎨 Dot Art Image Renderer

Turn any image into elegant **dot-style ASCII art** using Python. This renderer uses the pixel brightness of an image to draw dots of varying sizes, creating a clean, minimalistic output saved as a `.jpg` file. 

Perfect for artistic experimentation, retro visuals, and lightweight aesthetic renderings. Just give it an image path, and it handles the rest — no external tools needed besides `Pillow`.

---

## 📸 Features

- ✅ **Supports all common image formats** (JPG, PNG, BMP, etc.)
- 🎯 **Flexible input**: You enter the image path at runtime
- 🎨 **Grayscale-based dot sizing** — darker pixels = bigger dots
- ⚡ **Optimized for performance** — fast rendering
- 📂 **Output saved as a `.jpg`** automatically in the same folder
- 🐍 Written in **pure Python**, only one dependency (`Pillow`)
- 💡 Clean modular code — easy to modify and extend

---

## 🛠 How It Works

### Behind the scenes:

1. **User Input**  
   - You’re asked to enter the full path of your image (any format).
  
2. **Image Preprocessing**  
   - Image is resized to a fixed width (default: `100px`) to speed up rendering and scale proportionally.
   - Then, it's converted to **grayscale**, where each pixel has a value between `0` (black) and `255` (white).

3. **Dot Rendering**  
   - Each pixel’s brightness determines the **radius of a black dot** drawn on a white canvas.
   - **Darker pixels** → larger dots.  
   - **Lighter pixels** → smaller or no dots.

4. **Final Image**  
   - The result is saved as `dot_art_output.jpg` in the **same directory** as the input image.

---

## 🚀 Getting Started

### 1. Install Dependencies

You only need one Python library:

```bash
pip install pillow
