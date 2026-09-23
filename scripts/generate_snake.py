#!/usr/bin/env python3
"""Build a contribution-grid SVG from the public GitHub calendar."""

from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import html


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://github.com/users/wowito68/contributions"
DESTINATION = ROOT / "assets" / "snake.svg"
COLORS = ("#3b4a53", "#286d77", "#3b9ca6", "#67c8ce", "#a3efed")
MONTHS = ("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic")


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = []

    def handle_starttag(self, tag, attrs):
        if tag != "td":
            return
        values = dict(attrs)
        if "ContributionCalendar-day" not in values.get("class", ""):
            return
        try:
            day = date.fromisoformat(values["data-date"])
            level = max(0, min(4, int(values["data-level"])))
        except (KeyError, ValueError):
            return
        self.days.append((day, level))


def render(days):
    if len(days) < 300:
        raise RuntimeError(f"GitHub devolvió solo {len(days)} días de actividad")
    days = sorted(set(days))
    first = days[0][0]
    offset = (first.weekday() + 1) % 7  # Sunday = 0
    week_count = max(((day - first).days + offset) // 7 for day, _ in days) + 1
    left, top, step, size = 43, 33, 15, 11
    width = left + week_count * step + 17
    height = top + 7 * step + 21

    blocks = []
    for day, level in days:
        n = (day - first).days + offset
        week, weekday = divmod(n, 7)
        x, y = left + week * step, top + weekday * step
        title = html.escape(f"{day.isoformat()}: intensidad {level} de 4")
        blocks.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="2" fill="{COLORS[level]}"><title>{title}</title></rect>')

    labels = []
    seen = set()
    for day, _ in days:
        key = (day.year, day.month)
        if key in seen:
            continue
        seen.add(key)
        week = ((day - first).days + offset) // 7
        if week >= 2 and week + 3 <= week_count:
            labels.append(f'<text x="{left + week * step}" y="19">{MONTHS[day.month - 1]}</text>')

    # A single serpentine route gives the animated segment one continuous path.
    route = [f"M {left + 5} {top + 5}"]
    for row in range(7):
        end = left + (week_count - 1) * step + 5 if row % 2 == 0 else left + 5
        route.append(f"L {end} {top + row * step + 5}")
        if row < 6:
            route.append(f"L {end} {top + (row + 1) * step + 5}")
    path = " ".join(route)
    distance = (week_count - 1) * step * 7 + 6 * step
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Contribuciones de GitHub de Guillermo Álvarez</title>
<desc id="desc">Calendario público de {first.isoformat()} a {days[-1][0].isoformat()}, con una línea animada que lo recorre.</desc>
<style>
text{{font:11px system-ui,sans-serif;fill:#9ba9b0}}
.snake{{fill:none;stroke:#b3faf4;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:62 {distance};animation:travel 15s linear infinite;filter:drop-shadow(0 0 5px #62d7dc)}}
@keyframes travel{{to{{stroke-dashoffset:-{distance + 62}}}}}
@media(prefers-reduced-motion:reduce){{.snake{{animation:none;stroke-dashoffset:0}}}}
</style>
<g>{''.join(labels)}</g>
<g>{''.join(blocks)}</g>
<path class="snake" d="{path}"/>
</svg>
'''
    DESTINATION.write_text(svg, encoding="utf-8")
    print(f"SVG actualizado: {len(days)} días, {week_count} semanas → {DESTINATION}")


def main():
    request = Request(SOURCE, headers={"User-Agent": "wowito68-github-pages-site"})
    with urlopen(request, timeout=20) as response:
        markup = response.read().decode("utf-8")
    parser = CalendarParser()
    parser.feed(markup)
    render(parser.days)


if __name__ == "__main__":
    main()
