#!/usr/bin/env python3
"""Generate the charts for the AI-lag post as inline SVG, in both languages.

    python3 script/make_charts.py

Written as SVG rather than raster so the labels stay sharp and, more usefully,
so text and axes can be currentColor: inlined via {% include %} the charts
inherit the page's ink colour and follow the site's light/dark toggle. An SVG
referenced through <img> is an isolated document and cannot see the toggle.

Series colours are fixed and chosen to hold up on both backgrounds; everything
else (text, axes, grid) is currentColor.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("en", "zh")

PURPLE, LAV = "#5b4fc4", "#c3bcee"
ORANGE, BLUE, GREEN, AMBER = "#d95f2b", "#2274bd", "#17a07a", "#c08419"
# The CJK families are appended for both languages: an English chart may still
# contain a Chinese glyph, and the fallback costs nothing.
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")


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


def write(lang, name, s):
    d = os.path.join(ROOT, "_includes", "charts", "ai-lag", lang)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, name), "w", encoding="utf-8").write(s)
    print("  %s/%-9s %5d bytes" % (lang, name, len(s)))


# ---------------------------------------------------------------------------
# Label table. The Chinese strings are the ones on the author's original
# charts; the English are their translations.
# ---------------------------------------------------------------------------
STR = {
 "en": {
  "f1_title": "Three industrial revolutions and AI: the lag from commercialisation "
              "to broad adoption and measured productivity",
  "f1_rows": [("Steam (UK)", "1776 Watt engine → 1850–1870 peak"),
              ("Electricity (US)", "1882 Pearl Street → 1920s jump"),
              ("IT (US)", "1981 PC → 1995–2005 acceleration"),
              ("AI (projected)", "2022 ChatGPT → 2032–2035 deployment")],
  "f1_years": "%d years", "f1_x": "Years from commercialisation",
  "f1_leg1": "Commercialisation → adoption threshold",
  "f1_leg2": "Adoption threshold → productivity visible",
  "f2_title": "Britain's fixed power: steam vs water (Kanefsky / Crafts)",
  "f2_steam": "Steam", "f2_water": "Water (approx.)",
  "f2_y": "Installed horsepower, thousands (log scale)",
  "f2_note": "Watt's patent 1769 → level pegging around 1830 → "
             "high-pressure steam delivers after 1850",
  "f3_title": "The same machine, different factor prices (Allen 2009)",
  "f3_note": "Britain ~20,000 jennies by 1788; France ~900 by 1790; India 0",
  "f3_y": "Return on investment in a spinning jenny (%)",
  "f3_bars": [("Britain", "≈38%"), ("France", "≈9%"), ("India", "negative")],
  "f4_title": "US manufacturing electrification: productivity only jumps once "
              "the share passes about 50%",
  "f4_sub": "Devine 1983 / David 1990",
  "f4_a1": "1900–19: motors bolted to the line shaft",
  "f4_a2": "or group drive — TFP under 1%/yr",
  "f4_b1": "1919–29: unit drive spreads", "f4_b2": "manufacturing TFP above 5%/yr",
  "f4_y": "Electric motors as a share of manufacturing mechanical power (%)",
  "f5_title": "US firms using AI (Census BTOS, Dec 2025 – May 2026)",
  "f5_rows": ["1–4 employees", "All firms", "Employment-weighted",
              "100–249 employees", "250+ employees",
              "Information / professional\nservices / finance, large firms"],
  "f5_x": "Share of firms using AI in production over the previous two weeks",
  "f5_note": "57% of adopters use it in three or fewer business functions — "
             "shallow, “bolted to the line shaft” adoption",
  "f6_title": "Capex of the four hyperscalers (2023–24 approximate)",
  "f6_note": "Installation-period signature: financial capital leads, infrastructure "
             "is built ahead of demand, power becomes the binding constraint",
  "f6_y": "US$ billions",
  "f7_title": "The AI wave's productivity J-curve and Perez phases "
              "(synthesised projection, schematic)",
  "f7_bands": [("Installation, early", "Compute arms race"),
               ("Bottleneck and turn", "Energy and data bind, valuations reset"),
               ("Organisational rebuild", "Unit-drive-style redesign"),
               ("Full deployment", "TFP shows up")],
  "f7_trough": "J-curve trough: complementary intangible investment is expensed, "
               "not capitalised",
  "f7_y": "Measured productivity contribution (schematic)",
 },
 "zh": {
  "f1_title": "三次工业革命与 AI：从商业化到广泛采用与生产率显现的迟滞",
  "f1_rows": [("蒸汽（英国）", "1776 首台商用瓦特机 → 1850–1870 贡献峰值"),
              ("电力（美国）", "1882 珍珠街 → 1920s 生产率跃升"),
              ("信息技术（美国）", "1981 PC → 1995–2005 生产率加速"),
              ("AI（预测）", "2022 ChatGPT → 2032–2035 部署期")],
  "f1_years": "%d 年", "f1_x": "自商业化起点起的年数",
  "f1_leg1": "商业化 → 采用临界", "f1_leg2": "采用临界 → 生产率显现",
  "f2_title": "英国固定动力：蒸汽 vs 水力（Kanefsky / Crafts）",
  "f2_steam": "蒸汽", "f2_water": "水力（约）",
  "f2_y": "装机马力（千，对数轴）",
  "f2_note": "瓦特专利 1769 → 1830 年前后持平 → 1850 年后高压蒸汽兑现潜力",
  "f3_title": "同一台机器，不同要素价格下的回报（Allen 2009）",
  "f3_note": "英国 1788 年约 20,000 台；法国 1790 年约 900 台；印度 0",
  "f3_y": "珍妮纺纱机投资回报率（%）",
  "f3_bars": [("英国", "≈38%"), ("法国", "≈9%"), ("印度", "为负")],
  "f4_title": "美国制造业电气化：份额跨过约 50% 后生产率才跃升",
  "f4_sub": "Devine 1983 / David 1990",
  "f4_a1": "1900–19：电机接总轴／分组驱动", "f4_a2": "TFP 年增 <1%",
  "f4_b1": "1919–29：单机驱动普及", "f4_b2": "制造业 TFP 年增 >5%",
  "f4_y": "电动机占制造业机械动力比例（%）",
  "f5_title": "美国企业 AI 使用率（Census BTOS，2025.12–2026.05）",
  "f5_rows": ["1–4 人", "总体", "就业加权", "100–249 人", "250 人以上",
              "信息／专业服务／金融\n大企业"],
  "f5_x": "过去两周在业务职能中使用 AI 的企业比例",
  "f5_note": "采用者中 57% 仅在 ≤3 个业务职能使用 ——「接总轴」式浅层采用",
  "f6_title": "四大超大规模云厂商资本开支（2023–24 为约数）",
  "f6_note": "安装期特征：金融资本主导、基础设施超前建设；电力成为硬约束",
  "f6_y": "十亿美元",
  "f7_title": "AI 浪潮的生产力 J 曲线与 Perez 阶段（融合预测，示意）",
  "f7_bands": [("安装期初期", "算力军备竞赛"),
               ("瓶颈与转折", "能源／数据掣肘，估值调整"),
               ("组织重构期", "单机驱动式重建"),
               ("全面部署期", "TFP 显现")],
  "f7_trough": "J 曲线谷底：互补无形投资被记为费用",
  "f7_y": "可测生产率贡献（示意）",
 },
}


# --- fig 1: lag from commercialisation to productivity ---------------------
def fig1(lang):
    T = STR[lang]
    spans = [(54, 25), (37, 6), (14, 5), (8, 3)]
    W, H = 1080, 510
    x0, x1, top, bh, gap = 190, 940, 74, 40, 58
    sx = (x1 - x0) / 100.0
    b = [txt(150, 34, T["f1_title"], 17, weight="600")]
    for i, ((lab, note), (a, c)) in enumerate(zip(T["f1_rows"], spans)):
        y = top + i * (bh + gap)
        b.append(txt(x0 - 14, y + bh / 2 + 5, lab, 14, "end"))
        b.append(rect(x0, y, a * sx, bh, LAV))
        b.append(rect(x0 + a * sx, y, c * sx, bh, PURPLE))
        b.append(txt(x0 + a * sx / 2, y + bh / 2 + 5, T["f1_years"] % a, 14, "middle",
                     fill="#2b2560"))
        b.append(txt(x0 + a * sx + c * sx / 2, y + bh / 2 + 5, "+%d" % c, 13, "middle",
                     fill="#ffffff"))
        b.append(txt(x0 + (a + c) * sx + 12, y + bh / 2 + 5, note, 12.5, op=".6"))
    ay = top + 4 * (bh + gap) - gap + 22
    b.append(line(x0, ay, x1, ay, ".35"))
    for v in range(0, 101, 20):
        b.append(line(x0 + v * sx, ay, x0 + v * sx, ay + 6, ".35"))
        b.append(txt(x0 + v * sx, ay + 24, str(v), 13, "middle", op=".7"))
    b.append(txt((x0 + x1) / 2, ay + 48, T["f1_x"], 13, "middle", op=".7"))
    lx, ly = x0 + 430, top + 3 * (bh + gap) - 16
    b.append(rect(lx, ly, 22, 12, LAV))
    b.append(txt(lx + 30, ly + 11, T["f1_leg1"], 12.5, op=".75"))
    b.append(rect(lx, ly + 22, 22, 12, PURPLE))
    b.append(txt(lx + 30, ly + 33, T["f1_leg2"], 12.5, op=".75"))
    return svg(W, H, "\n".join(b), T["f1_title"])


# --- fig 2: steam vs water, log scale --------------------------------------
def fig2(lang):
    import math
    T = STR[lang]
    data = [("1800", 35, 120), ("1830", 160, 165), ("1870", 1700, 230)]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 150, 1030, 78, 452
    lo, hi = math.log10(25), math.log10(2600)

    def ypx(v):
        return ybot - (math.log10(v) - lo) / (hi - lo) * (ybot - ytop)

    b = [txt(110, 36, T["f2_title"], 17, weight="600")]
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
    for i, (yr, st, wt) in enumerate(data):
        cx = x0 + gw * (i + .5)
        for j, (v, col) in enumerate(((st, ORANGE), (wt, BLUE))):
            bx = cx - 130 + j * 132
            b.append(rect(bx, ypx(v), 118, ybot - ypx(v), col))
            b.append(txt(bx + 59, ypx(v) - 10, "%dk" % v, 13.5, "middle", weight="600"))
        b.append(txt(cx, ybot + 28, yr, 15, "middle"))
    b.append(rect(x0 + 28, ytop + 12, 24, 14, ORANGE))
    b.append(txt(x0 + 60, ytop + 24, T["f2_steam"], 14))
    b.append(rect(x0 + 28, ytop + 38, 24, 14, BLUE))
    b.append(txt(x0 + 60, ytop + 50, T["f2_water"], 14))
    b.append(txt(38, 300, T["f2_y"], 13, "middle", op=".75",
                 extra=' transform="rotate(-90 38 300)"'))
    b.append(txt((x0 + x1) / 2, ybot + 66, T["f2_note"], 13, "middle", op=".65"))
    return svg(W, H, "\n".join(b), T["f2_title"])


# --- fig 3: Allen factor prices --------------------------------------------
def fig3(lang):
    T = STR[lang]
    vals = [(38, GREEN), (9, AMBER), (-3.5, ORANGE)]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 140, 1030, 96, 470
    vmax, vmin = 45, -10

    def ypx(v):
        return ybot - (v - vmin) / (vmax - vmin) * (ybot - ytop)

    b = [txt(120, 36, T["f3_title"], 17, weight="600"),
         txt(160, 74, T["f3_note"], 13, op=".6")]
    for v in range(-10, 41, 10):
        b.append(line(x0, ypx(v), x1, ypx(v), ".08"))
        b.append(txt(x0 - 12, ypx(v) + 5, str(v), 13, "end", op=".7"))
    zero = ypx(0)
    b.append(line(x0, zero, x1, zero, ".45"))
    gw = (x1 - x0) / 3.0
    for i, ((lab, note), (v, col)) in enumerate(zip(T["f3_bars"], vals)):
        cx = x0 + gw * (i + .5)
        y = ypx(v) if v > 0 else zero
        b.append(rect(cx - 90, y, 180, abs(ypx(v) - zero), col))
        b.append(txt(cx, (ypx(v) - 12) if v > 0 else (ypx(v) + 26), note, 15, "middle",
                     weight="600"))
        b.append(txt(cx, ybot + 30, lab, 15, "middle"))
    b.append(txt(28, 290, T["f3_y"], 13, "middle", op=".75",
                 extra=' transform="rotate(-90 28 290)"'))
    return svg(W, H, "\n".join(b), T["f3_title"])


# --- fig 4: US electrification ---------------------------------------------
def fig4(lang):
    T = STR[lang]
    pts = [(1899, 5), (1909, 25), (1919, 53), (1929, 78)]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 150, 1020, 88, 470

    def xpx(y):
        return x0 + (y - 1899) / 30.0 * (x1 - x0)

    def ypx(v):
        return ybot - v / 90.0 * (ybot - ytop)

    b = [txt(130, 34, T["f4_title"], 17, weight="600"),
         txt(130, 56, T["f4_sub"], 13, op=".6")]
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
    b.append(txt(xpx(1904) + 20, ypx(62), T["f4_a1"], 13, "middle", op=".7"))
    b.append(txt(xpx(1904) + 20, ypx(56), T["f4_a2"], 13, "middle", op=".7"))
    b.append(txt((xpx(1919) + xpx(1929)) / 2, ytop + 24, T["f4_b1"], 13, "middle",
                 weight="600", op=".85"))
    b.append(txt((xpx(1919) + xpx(1929)) / 2, ytop + 42, T["f4_b2"], 13, "middle", op=".8"))
    b.append(txt(30, 290, T["f4_y"], 12.5, "middle", op=".75",
                 extra=' transform="rotate(-90 30 290)"'))
    return svg(W, H, "\n".join(b), T["f4_title"])


# --- fig 5: AI adoption -----------------------------------------------------
def fig5(lang):
    T = STR[lang]
    vals = [(18, "<20%", "#cfcbc4"), (18.5, "17–20%", "#8b8781"),
            (32, "32%", PURPLE), (32, "32%", PURPLE), (37, "37%", PURPLE),
            (55, "50–60%", GREEN)]
    W, H = 1080, 560
    x0, x1, top, bh, gap = 330, 950, 92, 34, 26
    sx = (x1 - x0) / 70.0
    b = [txt(300, 36, T["f5_title"], 17, weight="600")]
    for i, (lab, (v, note, col)) in enumerate(zip(T["f5_rows"], vals)):
        y = top + i * (bh + gap)
        lines = lab.split("\n")
        for k, l in enumerate(lines):
            b.append(txt(x0 - 16, y + bh / 2 + 5 - (len(lines) - 1) * 8 + k * 16, l, 13.5, "end"))
        b.append(rect(x0, y, v * sx, bh, col))
        b.append(txt(x0 + v * sx + 12, y + bh / 2 + 5, note, 13.5, weight="600"))
    ay = top + len(vals) * (bh + gap) - gap + 16
    b.append(line(x0, ay, x1, ay, ".35"))
    for v in range(0, 71, 10):
        b.append(line(x0 + v * sx, ay, x0 + v * sx, ay + 6, ".35"))
        b.append(txt(x0 + v * sx, ay + 24, str(v), 13, "middle", op=".7"))
    b.append(txt((x0 + x1) / 2, ay + 48, T["f5_x"], 13, "middle", op=".7"))
    # The original had this note overlapping the bar labels; it sits on its own line here.
    b.append(txt(300, 64, T["f5_note"], 13, op=".6"))
    return svg(W, H, "\n".join(b), T["f5_title"])


# --- fig 6: hyperscaler capex ----------------------------------------------
def fig6(lang):
    T = STR[lang]
    data = [("2023", 150, LAV, "≈150"), ("2024", 230, LAV, "≈230"),
            ("2025", 388, PURPLE, "388"), ("2026E", 630, ORANGE, "≈630")]
    W, H = 1080, 560
    x0, x1, ytop, ybot = 150, 1030, 96, 470

    def ypx(v):
        return ybot - v / 700.0 * (ybot - ytop)

    b = [txt(130, 36, T["f6_title"], 17, weight="600"),
         txt(180, 74, T["f6_note"], 12.5, op=".6")]
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
    b.append(txt(28, 290, T["f6_y"], 13, "middle", op=".75",
                 extra=' transform="rotate(-90 28 290)"'))
    return svg(W, H, "\n".join(b), T["f6_title"])


# --- fig 7: J curve ---------------------------------------------------------
def fig7(lang):
    T = STR[lang]
    W, H = 1080, 500
    x0, x1, ytop, ybot = 110, 1040, 60, 410

    def xpx(y):
        return x0 + (y - 2022) / 14.0 * (x1 - x0)

    spans = [(2022, 2025.5, "#8b8781"), (2025.5, 2028.5, ORANGE),
             (2028.5, 2031.5, PURPLE), (2031.5, 2036, GREEN)]
    b = [txt(90, 30, T["f7_title"], 16, weight="600")]
    for (a, c, col), (t1, t2) in zip(spans, T["f7_bands"]):
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
    b.append(txt(xpx(2027.4), base + 102, T["f7_trough"], 12.5, "middle", op=".7",
                 fill=ORANGE))
    b.append(line(x0, ybot, x1, ybot, ".35"))
    for y in range(2022, 2037, 2):
        b.append(line(xpx(y), ybot, xpx(y), ybot + 6, ".35"))
        b.append(txt(xpx(y), ybot + 26, str(y), 13, "middle", op=".7"))
    b.append(txt(26, 235, T["f7_y"], 12.5, "middle", op=".75",
                 extra=' transform="rotate(-90 26 235)"'))
    return svg(W, H, "\n".join(b), T["f7_title"])


if __name__ == "__main__":
    for lang in LANGS:
        for n, f in (("fig1.svg", fig1), ("fig2.svg", fig2), ("fig3.svg", fig3),
                     ("fig4.svg", fig4), ("fig5.svg", fig5), ("fig6.svg", fig6),
                     ("fig7.svg", fig7)):
            write(lang, n, f(lang))
