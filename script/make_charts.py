#!/usr/bin/env python3
"""Generate the English charts for the AI-lag post as inline SVG.

    python3 script/make_charts.py

The Chinese post keeps the author's original PNGs. The English versions are
rebuilt here so the labels can be in English — and as SVG rather than raster,
so they stay sharp and inherit the page's ink colour, which means they follow
the site's light/dark toggle. They are inlined via {% include %}: an SVG
referenced through <img> is an isolated document and cannot see the toggle.

Series colours are fixed and chosen to hold up on both backgrounds; everything
else (text, axes, grid) is currentColor.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "_includes", "charts", "ai-lag")

PURPLE, LAV = "#5b4fc4", "#c3bcee"
ORANGE, BLUE, GREEN, AMBER = "#d95f2b", "#2274bd", "#17a07a", "#c08419"
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,sans-serif\"")


def svg(w, h, body, desc):
    return (
        '<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
        '  <title>%s</title>\n%s\n</svg>\n' % (w, h, desc, FONT, desc, body))


def esc(s):
    """A label such as "<20%" is a raw < in text content — invalid markup."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=14, anchor="start", weight="400", op="1", fill="currentColor",
        extra=""):
    return ('  <text x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" '
            'font-weight="%s" fill="%s" fill-opacity="%s"%s>%s</text>'
            % (x, y, size, anchor, weight, fill, op, extra, esc(s)))


def line(x1, y1, x2, y2, op=".25", w=1):
    return ('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" '
            'stroke-opacity="%s" stroke-width="%s"/>' % (x1, y1, x2, y2, op, w))


def rect(x, y, w, h, fill, extra=""):
    return '  <rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"%s/>' % (
        x, y, max(w, 0), max(h, 0), fill, extra)


def write(name, s):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(s)
    print("  %-12s %5d bytes" % (name, len(s)))


# --- fig 1: lag from commercialisation to productivity ---------------------
def fig1():
    rows = [("Steam (UK)", 54, 25, "1776 Watt engine → 1850–1870 peak"),
            ("Electricity (US)", 37, 6, "1882 Pearl Street → 1920s jump"),
            ("IT (US)", 14, 5, "1981 PC → 1995–2005 acceleration"),
            ("AI (projected)", 8, 3, "2022 ChatGPT → 2032–2035 deployment")]
    W, H = 1080, 510
    x0, x1, top, bh, gap = 190, 940, 74, 40, 58
    sx = (x1 - x0) / 100.0
    b = [txt(150, 34, "Three industrial revolutions and AI: the lag from commercialisation "
                      "to broad adoption and measured productivity", 17, weight="600")]
    for i, (lab, a, c, note) in enumerate(rows):
        y = top + i * (bh + gap)
        b.append(txt(x0 - 14, y + bh / 2 + 5, lab, 14, "end"))
        b.append(rect(x0, y, a * sx, bh, LAV))
        b.append(rect(x0 + a * sx, y, c * sx, bh, PURPLE))
        b.append('  <text x="%.1f" y="%.1f" font-size="14" text-anchor="middle" fill="#2b2560">%d years</text>'
                 % (x0 + a * sx / 2, y + bh / 2 + 5, a))
        b.append('  <text x="%.1f" y="%.1f" font-size="13" text-anchor="middle" fill="#ffffff">+%d</text>'
                 % (x0 + a * sx + c * sx / 2, y + bh / 2 + 5, c))
        b.append(txt(x0 + (a + c) * sx + 12, y + bh / 2 + 5, note, 12.5, op=".6"))
    ay = top + 4 * (bh + gap) - gap + 22
    b.append(line(x0, ay, x1, ay, ".35"))
    for v in range(0, 101, 20):
        b.append(line(x0 + v * sx, ay, x0 + v * sx, ay + 6, ".35"))
        b.append(txt(x0 + v * sx, ay + 24, str(v), 13, "middle", op=".7"))
    b.append(txt((x0 + x1) / 2, ay + 48, "Years from commercialisation", 13, "middle", op=".7"))
    lx, ly = x0 + 430, top + 3 * (bh + gap) - 16
    b.append(rect(lx, ly, 22, 12, LAV))
    b.append(txt(lx + 30, ly + 11, "Commercialisation → adoption threshold", 12.5, op=".75"))
    b.append(rect(lx, ly + 22, 22, 12, PURPLE))
    b.append(txt(lx + 30, ly + 33, "Adoption threshold → productivity visible", 12.5, op=".75"))
    return svg(W, H, "\n".join(b),
               "Bar chart of the lag from commercialisation to measured productivity for steam, "
               "electricity, IT and AI")


# --- fig 2: steam vs water, log scale --------------------------------------
def fig2():
    import math
    data = [("1800", 35, 120), ("1830", 160, 165), ("1870", 1700, 230)]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 150, 1030, 78, 452
    lo, hi = math.log10(25), math.log10(2600)

    def ypx(v):
        return ybot - (math.log10(v) - lo) / (hi - lo) * (ybot - ytop)

    b = [txt(110, 36, "Britain's fixed power: steam vs water (Kanefsky / Crafts)", 17, weight="600")]
    for e in (2, 3):
        for m in (1, 2, 3, 5):
            v = m * 10 ** e
            if 25 < v < 2600:
                b.append(line(x0, ypx(v), x1, ypx(v), ".08"))
    for e, lab in ((2, "100"), (3, "1,000")):
        b.append(txt(x0 - 12, ypx(10 ** e) + 5, lab, 13, "end", op=".7"))
    b.append(line(x0, ytop, x0, ybot, ".35"))
    b.append(line(x0, ybot, x1, ybot, ".35"))
    gw = (x1 - x0) / 3.0
    for i, (yr, s, w) in enumerate(data):
        cx = x0 + gw * (i + .5)
        for j, (v, col) in enumerate(((s, ORANGE), (w, BLUE))):
            bx = cx - 130 + j * 132
            b.append(rect(bx, ypx(v), 118, ybot - ypx(v), col))
            b.append(txt(bx + 59, ypx(v) - 10, "%dk" % v, 13.5, "middle", weight="600"))
        b.append(txt(cx, ybot + 28, yr, 15, "middle"))
    b.append(rect(x0 + 28, ytop + 12, 24, 14, ORANGE))
    b.append(txt(x0 + 60, ytop + 24, "Steam", 14))
    b.append(rect(x0 + 28, ytop + 38, 24, 14, BLUE))
    b.append(txt(x0 + 60, ytop + 50, "Water (approx.)", 14))
    b.append(txt(38, 300, "Installed horsepower, thousands (log scale)", 13, "middle",
                 op=".75", extra=' transform="rotate(-90 38 300)"'))
    b.append(txt((x0 + x1) / 2, ybot + 66,
                 "Watt's patent 1769 → level pegging around 1830 → "
                 "high-pressure steam delivers after 1850", 13, "middle", op=".65"))
    return svg(W, H, "\n".join(b),
               "Bar chart comparing installed steam and water horsepower in Britain in 1800, 1830 and 1870")


# --- fig 3: Allen factor prices --------------------------------------------
def fig3():
    data = [("Britain", 38, GREEN, "≈38%"), ("France", 9, AMBER, "≈9%"),
            ("India", -3.5, ORANGE, "negative")]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 140, 1030, 96, 470
    vmax, vmin = 45, -10

    def ypx(v):
        return ybot - (v - vmin) / (vmax - vmin) * (ybot - ytop)

    b = [txt(120, 36, "The same machine, different factor prices (Allen 2009)", 17, weight="600"),
         txt(160, 74, "Britain ~20,000 jennies by 1788; France ~900 by 1790; India 0", 13, op=".6")]
    for v in range(-10, 41, 10):
        b.append(line(x0, ypx(v), x1, ypx(v), ".08"))
        b.append(txt(x0 - 12, ypx(v) + 5, str(v), 13, "end", op=".7"))
    zero = ypx(0)
    b.append(line(x0, zero, x1, zero, ".45"))
    gw = (x1 - x0) / 3.0
    for i, (lab, v, col, note) in enumerate(data):
        cx = x0 + gw * (i + .5)
        y = ypx(v) if v > 0 else zero
        b.append(rect(cx - 90, y, 180, abs(ypx(v) - zero), col))
        b.append(txt(cx, (ypx(v) - 12) if v > 0 else (ypx(v) + 26), note, 15, "middle", weight="600"))
        b.append(txt(cx, ybot + 30, lab, 15, "middle"))
    b.append(txt(28, 290, "Return on investment in a spinning jenny (%)", 13, "middle",
                 op=".75", extra=' transform="rotate(-90 28 290)"'))
    return svg(W, H, "\n".join(b),
               "Bar chart of the return on investment in a spinning jenny in Britain, France and India")


# --- fig 4: US electrification ---------------------------------------------
def fig4():
    pts = [(1899, 5), (1909, 25), (1919, 53), (1929, 78)]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 150, 1020, 88, 470

    def xpx(y):
        return x0 + (y - 1899) / 30.0 * (x1 - x0)

    def ypx(v):
        return ybot - v / 90.0 * (ybot - ytop)

    b = [txt(130, 34, "US manufacturing electrification: productivity only jumps once the "
                      "share passes about 50%", 17, weight="600"),
         txt(130, 56, "Devine 1983 / David 1990", 13, op=".6")]
    b.append(rect(xpx(1919), ytop, xpx(1929) - xpx(1919), ybot - ytop, GREEN,
                  ' fill-opacity=".12"'))
    for v in range(0, 81, 20):
        b.append(line(x0, ypx(v), x1, ypx(v), ".08"))
        b.append(txt(x0 - 12, ypx(v) + 5, str(v), 13, "end", op=".7"))
    b.append(line(x0, ybot, x1, ybot, ".35"))
    d = " ".join(("M" if i == 0 else "L") + "%.1f %.1f" % (xpx(y), ypx(v))
                 for i, (y, v) in enumerate(pts))
    b.append('  <path d="%s" fill="none" stroke="%s" stroke-width="3.5" '
             'stroke-linejoin="round"/>' % (d, PURPLE))
    for y, v in pts:
        b.append('  <circle cx="%.1f" cy="%.1f" r="6" fill="%s"/>' % (xpx(y), ypx(v), PURPLE))
        b.append(txt(xpx(y), ypx(v) - 16, "%d%%" % v, 14, "middle", weight="600"))
        b.append(txt(xpx(y), ybot + 30, str(y), 15, "middle"))
    b.append(txt(xpx(1904) + 20, ypx(62), "1900–19: motors bolted to the line shaft", 13, "middle", op=".7"))
    b.append(txt(xpx(1904) + 20, ypx(56), "or group drive — TFP under 1%/yr", 13, "middle", op=".7"))
    b.append(txt((xpx(1919) + xpx(1929)) / 2, ytop + 24, "1919–29: unit drive spreads", 13, "middle",
                 weight="600", op=".85"))
    b.append(txt((xpx(1919) + xpx(1929)) / 2, ytop + 42, "manufacturing TFP above 5%/yr", 13, "middle",
                 op=".8"))
    b.append(txt(30, 290, "Electric motors as a share of manufacturing mechanical power (%)", 12.5,
                 "middle", op=".75", extra=' transform="rotate(-90 30 290)"'))
    return svg(W, H, "\n".join(b),
               "Line chart of electric motors as a share of US manufacturing power, 1899 to 1929")


# --- fig 5: AI adoption -----------------------------------------------------
def fig5():
    rows = [("1–4 employees", 18, "<20%", "#cfcbc4"),
            ("All firms", 18.5, "17–20%", "#8b8781"),
            ("Employment-weighted", 32, "32%", PURPLE),
            ("100–249 employees", 32, "32%", PURPLE),
            ("250+ employees", 37, "37%", PURPLE),
            ("Information / professional\nservices / finance, large firms", 55, "50–60%", GREEN)]
    W, H = 1080, 560
    x0, x1, top, bh, gap = 330, 950, 92, 34, 26
    sx = (x1 - x0) / 70.0
    b = [txt(300, 36, "US firms using AI (Census BTOS, Dec 2025 – May 2026)", 17, weight="600")]
    for i, (lab, v, note, col) in enumerate(rows):
        y = top + i * (bh + gap)
        lines = lab.split("\n")
        for k, l in enumerate(lines):
            b.append(txt(x0 - 16, y + bh / 2 + 5 - (len(lines) - 1) * 8 + k * 16, l, 13.5, "end"))
        b.append(rect(x0, y, v * sx, bh, col))
        b.append(txt(x0 + v * sx + 12, y + bh / 2 + 5, note, 13.5, weight="600"))
    ay = top + len(rows) * (bh + gap) - gap + 16
    b.append(line(x0, ay, x1, ay, ".35"))
    for v in range(0, 71, 10):
        b.append(line(x0 + v * sx, ay, x0 + v * sx, ay + 6, ".35"))
        b.append(txt(x0 + v * sx, ay + 24, str(v), 13, "middle", op=".7"))
    b.append(txt((x0 + x1) / 2, ay + 48,
                 "Share of firms using AI in production over the previous two weeks", 13, "middle", op=".7"))
    # The original had this note overlapping the bar labels; it sits on its own line here.
    b.append(txt(300, 64,
                 "57% of adopters use it in three or fewer business functions — shallow, "
                 "“bolted to the line shaft” adoption", 13, op=".6"))
    return svg(W, H, "\n".join(b),
               "Bar chart of the share of US firms using AI, by firm size and sector")


# --- fig 6: hyperscaler capex ----------------------------------------------
def fig6():
    data = [("2023", 150, LAV, "≈150"), ("2024", 230, LAV, "≈230"),
            ("2025", 388, PURPLE, "388"), ("2026E", 630, ORANGE, "≈630")]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 150, 1030, 96, 470

    def ypx(v):
        return ybot - v / 700.0 * (ybot - ytop)

    b = [txt(130, 36, "Capex of the four hyperscalers (2023–24 approximate)", 17, weight="600"),
         txt(180, 74, "Installation-period signature: financial capital leads, infrastructure is built "
                      "ahead of demand, power becomes the binding constraint", 12.5, op=".6")]
    for v in range(0, 701, 100):
        b.append(line(x0, ypx(v), x1, ypx(v), ".08"))
        b.append(txt(x0 - 12, ypx(v) + 5, str(v), 13, "end", op=".7"))
    b.append(line(x0, ybot, x1, ybot, ".35"))
    gw = (x1 - x0) / 4.0
    for i, (lab, v, col, note) in enumerate(data):
        cx = x0 + gw * (i + .5)
        b.append(rect(cx - 80, ypx(v), 160, ybot - ypx(v), col))
        b.append(txt(cx, ypx(v) - 12, note, 15, "middle", weight="600"))
        b.append(txt(cx, ybot + 30, lab, 15, "middle"))
    b.append(txt(28, 290, "US$ billions", 13, "middle", op=".75",
                 extra=' transform="rotate(-90 28 290)"'))
    return svg(W, H, "\n".join(b), "Bar chart of combined capital expenditure by the four hyperscalers")


# --- fig 7: J curve ---------------------------------------------------------
def fig7():
    W, H = 1080, 500
    x0, x1, ytop, ybot = 110, 1040, 60, 410

    def xpx(y):
        return x0 + (y - 2022) / 14.0 * (x1 - x0)

    bands = [(2022, 2025.5, "#8b8781", "Installation, early", "Compute arms race"),
             (2025.5, 2028.5, ORANGE, "Bottleneck and turn", "Energy and data bind, valuations reset"),
             (2028.5, 2031.5, PURPLE, "Organisational rebuild", "Unit-drive-style redesign"),
             (2031.5, 2036, GREEN, "Full deployment", "TFP shows up")]
    b = [txt(90, 30, "The AI wave's productivity J-curve and Perez phases "
                     "(synthesised projection, schematic)", 16, weight="600")]
    for a, c, col, t1, t2 in bands:
        b.append(rect(xpx(a), ytop, xpx(c) - xpx(a), ybot - ytop, col, ' fill-opacity=".10"'))
        mid = (xpx(a) + xpx(c)) / 2
        b.append(txt(mid, ytop + 22, t1, 13, "middle", weight="600", op=".85"))
        b.append(txt(mid, ytop + 40, t2, 12, "middle", op=".6"))
    base = ybot - 120
    b.append('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" '
             'stroke-opacity=".3" stroke-dasharray="5 5"/>' % (x0, base, x1, base))
    b.append('  <path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f '
             'S %.1f %.1f, %.1f %.1f S %.1f %.1f, %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="3.5"/>' % (
                 xpx(2022), base,
                 xpx(2024), base + 6, xpx(2026.2), base + 78, xpx(2027.4), base + 82,
                 xpx(2029.4), base + 40, xpx(2030.2), base - 30,
                 xpx(2033), base - 120, xpx(2036), base - 128, PURPLE))
    b.append(txt(xpx(2027.4), base + 102,
                 "J-curve trough: complementary intangible investment is expensed, not capitalised",
                 12.5, "middle", op=".7", fill=ORANGE))
    b.append(line(x0, ybot, x1, ybot, ".35"))
    for y in range(2022, 2037, 2):
        b.append(line(xpx(y), ybot, xpx(y), ybot + 6, ".35"))
        b.append(txt(xpx(y), ybot + 26, str(y), 13, "middle", op=".7"))
    b.append(txt(26, 235, "Measured productivity contribution (schematic)", 12.5, "middle",
                 op=".75", extra=' transform="rotate(-90 26 235)"'))
    return svg(W, H, "\n".join(b),
               "Schematic J-curve of AI productivity with four Perez phases from 2022 to 2036")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in (("fig1.svg", fig1), ("fig2.svg", fig2), ("fig3.svg", fig3),
                 ("fig4.svg", fig4), ("fig5.svg", fig5), ("fig6.svg", fig6),
                 ("fig7.svg", fig7)):
        write(n, f())
