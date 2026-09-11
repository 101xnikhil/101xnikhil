from PIL import Image, ImageOps

INPUT = "source-prepped.png"
OUTPUT = "nikhil-ascii.svg"

# Load image
img = Image.open(INPUT).convert("RGBA")

# Crop to the visible subject using alpha
alpha = img.getchannel("A")
bbox = alpha.getbbox()

if bbox:
    # Add a little padding around the subject
    w, h = img.size
    x1, y1, x2, y2 = bbox
    pad_x = int((x2 - x1) * 0.06)
    pad_y = int((y2 - y1) * 0.06)

    x1 = max(0, x1 - pad_x)
    y1 = max(0, y1 - pad_y)
    x2 = min(w, x2 + pad_x)
    y2 = min(h, y2 + pad_y)

    img = img.crop((x1, y1, x2, y2))

# Convert to grayscale
gray = ImageOps.grayscale(img)

# Stronger contrast
gray = ImageOps.autocontrast(gray)

# ASCII settings
cols = 90
char_ratio = 0.48

width, height = gray.size
rows = max(1, int(height / width * cols * char_ratio))

gray = gray.resize((cols, rows))

pixels = list(gray.getdata())

chars = " .:-=+*#%@"

lines = []

for y in range(rows):
    line = ""

    for x in range(cols):
        value = pixels[y * cols + x]

        # Invert so dark areas become dense ASCII
        index = int((255 - value) / 255 * (len(chars) - 1))

        line += chars[index]

    lines.append(line.rstrip())

# Build SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="900"
     height="{rows * 11 + 50}"
     viewBox="0 0 900 {rows * 11 + 50}">

<rect width="900" height="{rows * 11 + 50}" rx="14" fill="#0d1117"/>

<g fill="#c9d1d9"
   font-family="monospace"
   font-size="11"
   xml:space="preserve">'''

for i, line in enumerate(lines):
    svg += f'''
<text x="20" y="{35 + i * 11}">{line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</text>'''

svg += '''
</g>
</svg>
'''

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Created {OUTPUT}")