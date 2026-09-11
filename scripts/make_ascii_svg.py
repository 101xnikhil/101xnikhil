from PIL import Image

RAMP = " .`:-=+*cs#%@"

image = Image.open("cropped-source.png").convert("L")

width = 100
height = 53
image = image.resize((width, height))

lines = []

for y in range(height):
    line = ""

    for x in range(width):
        pixel = image.getpixel((x, y))
        index = pixel * (len(RAMP) - 1) // 255
        line += RAMP[index]

    lines.append(line)


svg = '''<svg xmlns="http://www.w3.org/2000/svg"
width="1000"
height="530"
viewBox="0 0 1000 530">

<rect width="100%" height="100%" fill="#0d1117"/>

<g fill="#c9d1d9"
   font-family="monospace"
   font-size="10"
   xml:space="preserve">
'''

for y, line in enumerate(lines):
    delay = y * 0.04

    svg += f'''
<text x="0" y="{(y + 1) * 10}">
    {line}
    <animate
        attributeName="opacity"
        from="0"
        to="1"
        begin="{delay:.2f}s"
        dur="0.08s"
        fill="freeze" />
</text>
'''

svg += '''
</g>

<!-- Blinking cursor -->
<rect x="0" y="525" width="6" height="10" fill="#c9d1d9">
    <animate
        attributeName="opacity"
        values="1;0;1"
        dur="0.8s"
        repeatCount="indefinite" />
</rect>

</svg>
'''

with open("nikhil-ascii.svg", "w") as f:
    f.write(svg)

print("Created animated nikhil-ascii.svg")