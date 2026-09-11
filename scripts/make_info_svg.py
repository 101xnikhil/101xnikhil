info = [
    ("OS", "macOS"),
    ("Host", "MacBook Air"),
    ("Role", "B.Tech Student"),
    ("Focus", "Software Development"),
    ("Languages", "Python • JavaScript • C++"),
    ("Tools", "Git • GitHub • VS Code"),
    ("Status", "Building & Learning")
]

svg = '''<svg xmlns="http://www.w3.org/2000/svg"
width="900"
height="530"
viewBox="0 0 900 530">

<rect width="100%" height="100%" rx="14" fill="#0d1117"/>

<text x="35" y="55"
fill="#58a6ff"
font-family="monospace"
font-size="28"
font-weight="bold">nikhil@github</text>
'''

y = 110

for key, value in info:
    svg += f'''
<text x="40" y="{y}"
fill="#58a6ff"
font-family="monospace"
font-size="20">{key}</text>

<text x="210" y="{y}"
fill="#c9d1d9"
font-family="monospace"
font-size="20">{value}</text>
'''
    y += 55

svg += '''
<text x="40" y="490"
fill="#8b949e"
font-family="monospace"
font-size="16">$ ./keep_building.sh</text>

</svg>
'''

with open("nikhil-info.svg", "w") as f:
    f.write(svg)

print("Created nikhil-info.svg")