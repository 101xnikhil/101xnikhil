import requests
from bs4 import BeautifulSoup

USERNAME = "101xnikhil"

url = f"https://github.com/users/{USERNAME}/contributions"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

days = soup.select("td.ContributionCalendar-day")

print(f"Found {len(days)} contribution days")

svg = '''<svg xmlns="http://www.w3.org/2000/svg"
width="860"
height="150"
viewBox="0 0 860 150">

<rect width="100%" height="100%" rx="12" fill="#0d1117"/>

<text x="20" y="30"
fill="#c9d1d9"
font-family="monospace"
font-size="16">
GitHub Contributions
</text>
'''

x = 20
y = 50

for i, day in enumerate(days[-364:]):
    level = day.get("data-level", "0")

    colors = {
        "0": "#161b22",
        "1": "#0e4429",
        "2": "#006d32",
        "3": "#26a641",
        "4": "#39d353",
    }

    color = colors.get(level, "#161b22")

    svg += f'''
<rect x="{x}" y="{y}"
      width="10" height="10"
      rx="2"
      fill="{color}"/>
'''

    x += 12

    if (i + 1) % 52 == 0:
        x = 20
        y += 14

svg += '''
</svg>
'''

with open("nikhil-heatmap.svg", "w") as f:
    f.write(svg)

print("Created nikhil-heatmap.svg")