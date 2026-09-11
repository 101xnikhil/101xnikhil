svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="490"
     height="530"
     viewBox="0 0 490 530">

<rect width="490" height="530" rx="14" fill="#0d1117"/>

<text x="30" y="50"
      fill="#58a6ff"
      font-family="monospace"
      font-size="25"
      font-weight="bold">nikhil@github</text>

<text x="30" y="75"
      fill="#8b949e"
      font-family="monospace"
      font-size="14">------------------------------</text>

<text x="30" y="120" fill="#58a6ff" font-family="monospace" font-size="17">OS</text>
<text x="170" y="120" fill="#c9d1d9" font-family="monospace" font-size="17">macOS</text>

<text x="30" y="165" fill="#58a6ff" font-family="monospace" font-size="17">Host</text>
<text x="170" y="165" fill="#c9d1d9" font-family="monospace" font-size="17">MacBook Air</text>

<text x="30" y="210" fill="#58a6ff" font-family="monospace" font-size="17">Role</text>
<text x="170" y="210" fill="#c9d1d9" font-family="monospace" font-size="17">B.Tech Student</text>

<text x="30" y="255" fill="#58a6ff" font-family="monospace" font-size="17">Focus</text>
<text x="170" y="255" fill="#c9d1d9" font-family="monospace" font-size="17">Software Development</text>

<text x="30" y="300" fill="#58a6ff" font-family="monospace" font-size="17">Languages</text>
<text x="170" y="300" fill="#c9d1d9" font-family="monospace" font-size="17">Python / JS / C++</text>

<text x="30" y="345" fill="#58a6ff" font-family="monospace" font-size="17">Tools</text>
<text x="170" y="345" fill="#c9d1d9" font-family="monospace" font-size="17">Git / GitHub / VS Code</text>

<text x="30" y="390" fill="#58a6ff" font-family="monospace" font-size="17">Status</text>
<text x="170" y="390" fill="#39d353" font-family="monospace" font-size="17">Building and Learning</text>

<text x="30" y="480"
      fill="#8b949e"
      font-family="monospace"
      font-size="15">$ ./keep_building.sh</text>

</svg>
'''

with open("nikhil-info.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Created nikhil-info.svg")
