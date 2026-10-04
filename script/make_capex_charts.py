#!/usr/bin/env python3
"""Generate the three charts for the AI-capex post as inline SVG, both languages.

    python3 script/make_capex_charts.py

The WeChat originals are rasters with Chinese labels burnt in. Redrawn for the
same reasons as script/make_charts.py: the English post needs its own labels,
and inlined via {% include %} text and axes are currentColor and follow the
site's light/dark toggle. The darkest series is currentColor too, so it inverts
with the page instead of vanishing on the dark background; the purples are
fixed, and purple text carries .accent-text so style.css can lighten it there.

Values are as published in the original figures (fig. 3's Micron bar shows
87.0% where the text gives 86.8% GAAP; the figure is kept as published).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P1, P2, P3, P4 = "#5b4fc4", "#8b80e6", "#b3abf0", "#d6d1f7"   # purple, dark → light
INK = "currentColor"
DARK_TEXT = "#1b1640"          # text sitting on a light purple bar, either theme
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=18, anchor="start", weight="400", fill=INK, op="1"):
    cls = ' class="accent-text"' if fill == P1 else ""
    return ('  <text%s x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" font-weight="%s" '
            'fill="%s" fill-opacity="%s">%s</text>'
            % (cls, x, y, size, anchor, weight, fill, op, esc(s)))


def rect(x, y, w, h, fill, op="1"):
    return ('  <rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity="%s"/>'
            % (x, y, max(w, 0), h, fill, op))


def line(x1, y1, x2, y2, op=".9", w=1.5, stroke=INK):
    return ('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-opacity="%s" stroke-width="%s"/>' % (x1, y1, x2, y2, stroke, op, w))


def svg(w, h, desc, body):
    return ('<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n' % (w, h, esc(desc), FONT, esc(desc),
                                                    "\n".join(body)))


def num(v):
    return ("%g" % v)


# ---------------------------------------------------------------- figure 1

LAYERS = {
    "zh": [("半导体芯片", 50, [("加速器", 25), ("存储", 15), ("CPU、其他芯片与服务器生产", 10)]),
           ("网络设备", 15, [("光模块", 5.5), ("交换机", 4.5), ("网络处理器", 3), ("线缆", 2)]),
           ("电力", 20, [("并网与自备发电", 10), ("配电", 6.5), ("场内电力布线", 3.5)]),
           ("冷却", 7.5, [("冷水机组与冷却塔", 2.5), ("冷量分配单元", 2), ("冷板", 1.5),
                          ("其他", 1.5)]),
           ("厂房与建设", 7.5, [("建筑主体与结构", 4), ("内部装修与配套", 2.5),
                               ("土地与选址", 1)])],
    "en": [("Semiconductors", 50, [("Accelerators", 25), ("Memory", 15),
                                   ("CPUs, other chips & server manufacturing", 10)]),
           ("Networking", 15, [("Optical modules", 5.5), ("Switches", 4.5),
                               ("Network processors", 3), ("Cables", 2)]),
           ("Power", 20, [("Grid connection & on-site generation", 10),
                          ("Power distribution", 6.5), ("On-site electrical wiring", 3.5)]),
           ("Cooling", 7.5, [("Chillers & cooling towers", 2.5),
                             ("Coolant distribution units", 2), ("Cold plates", 1.5),
                             ("Other", 1.5)]),
           ("Buildings & construction", 7.5, [("Shell & structure", 4),
                                              ("Fit-out & services", 2.5),
                                              ("Land & site", 1)])],
}
F1 = {
    "zh": {"title": "一笔 100 美元 AI 资本开支的去向（券商估算）",
           "wfe": "第二层流动：晶圆厂设备（WFE）标注 8",
           "wfe_note": "由芯片厂商用收入支付，不应与上面的 100 相加；原图各分项合计为 18，与 8 不符",
           "foot": "单位：美元。数据为 BNP Paribas 股票研究的高层级估算（2026 年 8 月，"
                   "经 a16z Growth 转引），一目半重新绘制"},
    "en": {"title": "Where $100 of AI capex goes (broker estimate)",
           "wfe": "Second-tier flow: wafer fab equipment (WFE), labelled 8",
           "wfe_note": "Paid by chipmakers out of revenue, so not additive to the 100 above; "
                       "the original's sub-items sum to 18, not 8",
           "foot": "Units: US dollars. High-level estimates from BNP Paribas Equity Research "
                   "(Aug 2026, via a16z Growth), redrawn by 一目半 (Yimuban)"},
}
TOP_COLOURS = [INK, P1, P2, P3, P4]


def fig1(lang):
    t, layers = F1[lang], LAYERS[lang]
    x0, unit = 40, 10.0                # 100 units span 1000 px
    out = [txt(x0, 58, t["title"], 26, weight="600")]
    # the whole $100, one stacked bar
    x = x0
    for (name, v, _), c in zip(layers, TOP_COLOURS):
        w = v * unit
        out.append(rect(x, 100, w - 2, 54, c, ".92" if c == INK else "1"))
        label_fill = "#fff" if c in (P1, P2) else DARK_TEXT
        if c == INK:   # inverted ink bar: text in the page background colour
            out.append('  <text x="%.1f" y="%.1f" font-size="20" text-anchor="middle" '
                       'style="fill: var(--bg, #fff)">%s</text>' % (x + w / 2, 134, num(v)))
        else:
            out.append(txt(x + w / 2, 134, num(v), 18 if v < 10 else 20, "middle",
                           fill=label_fill))
        x += w
    # one block per layer
    y = 210
    sub_unit = 14.0
    for (name, v, subs), c in zip(layers, TOP_COLOURS):
        out.append(rect(x0, y - 24, 12, 28, c, ".92" if c == INK else "1"))
        out.append('  <text x="%.1f" y="%.1f" font-size="24" fill="currentColor">'
                   '%s <tspan font-weight="700">%s</tspan></text>'
                   % (x0 + 24, y, esc(name), num(v)))
        xx = x0
        for i, (_, sv) in enumerate(subs):
            w = sv * sub_unit
            out.append(rect(xx, y + 28, w - 2, 28, P1 if i % 2 == 0 else P3))
            xx += w
        # en spaces: SVG collapses runs of ordinary spaces into one
        label = "\u2002·\u2002".join("%s %s" % (n, num(sv)) for n, sv in subs)
        out.append(txt(x0, y + 92, label, 19))
        y += 140
    # WFE note
    y += 2
    out.append(line(x0, y - 30, 1040, y - 30, ".4", 1.5, P1))
    out += [txt(x0, y + 4, t["wfe"], 21, weight="600", fill=P1),
            txt(x0, y + 40, t["wfe_note"], 18),
            txt(x0, y + 82, t["foot"], 16, op=".7")]
    return svg(1080, y + 104, t["title"], out)


# ---------------------------------------------------------------- figure 2

F2 = {
    "zh": {"title": "每 100 美元：支出份额 vs 估算毛利份额",
           "spend": "支出份额（图 1）", "margin": "估算毛利份额",
           "rows": ["加速器", "存储", "CPU 与服务器", "网络", "电力", "冷却", "厂房与建设"],
           "foot": ["毛利份额按各层代表性公司最近一季毛利率估算；电力、冷却、建筑的毛利率为作者假设"]},
    "en": {"title": "Per $100: share of spending vs estimated share of gross profit",
           "spend": "Share of spending (fig. 1)", "margin": "Estimated share of gross profit",
           "rows": ["Accelerators", "Memory", "CPUs & servers", "Networking", "Power",
                    "Cooling", "Buildings"],
           "foot": ["Gross-profit shares use each layer's representative companies' "
                    "latest-quarter gross margins;",
                    "margins for power, cooling and buildings are the author's assumptions"]},
}
F2_VALUES = [(25, 38), (15, 24), (10, 5), (15, 15), (20, 10), (7.5, 5), (7.5, 2)]


def fig2(lang):
    t = F2[lang]
    ax, unit = 260, 14.0
    out = [txt(40, 58, t["title"], 26, weight="600"),
           rect(40, 88, 26, 22, P3), txt(76, 106, t["spend"], 19),
           rect(lang == "zh" and 300 or 360, 88, 26, 22, P1),
           txt((lang == "zh" and 300 or 360) + 36, 106, t["margin"], 19)]
    y = 160
    for name, (s, m) in zip(t["rows"], F2_VALUES):
        out.append(txt(40, y + 24, name, 21))
        out += [rect(ax, y, s * unit, 26, P3), txt(ax + s * unit + 10, y + 20, "%s%%" % num(s), 17),
                rect(ax, y + 30, m * unit, 26, P1),
                txt(ax + m * unit + 10, y + 50, "%s%%" % num(m), 17)]
        y += 90
    out.append(line(ax, 145, ax, y - 20))
    for i, row in enumerate(t["foot"]):
        out.append(txt(40, y + 20 + i * 26, row, 16, op=".75"))
    return svg(1080, y + 20 + len(t["foot"]) * 26, t["title"], out)


# ---------------------------------------------------------------- figure 3

F3 = {
    "zh": {"title": "最近一个季度毛利率",
           "rows": ["美光（存储）", "英伟达（加速器）", "博通（定制芯片）", "台积电（代工）",
                    "Arista（交换机）", "ASML（光刻）", "Coherent（光模块）", "鸿海（整机组装）"],
           "approx": "约 ",
           "foot": ["美光、台积电、ASML、鸿海为 GAAP 或公司口径；英伟达 GAAP 与非 GAAP 相同；",
                    "博通、Arista、Coherent 为非 GAAP"]},
    "en": {"title": "Gross margin, latest quarter",
           "rows": ["Micron (memory)", "Nvidia (accelerators)", "Broadcom (custom chips)",
                    "TSMC (foundry)", "Arista (switches)", "ASML (lithography)",
                    "Coherent (optical modules)", "Foxconn (server assembly)"],
           "approx": "~",
           "foot": ["Micron, TSMC, ASML and Foxconn: GAAP or company basis; Nvidia: GAAP and "
                    "non-GAAP identical;", "Broadcom, Arista and Coherent: non-GAAP"]},
}
F3_VALUES = [(87.0, P1, False), (75.0, P1, False), (75, P1, True), (67.7, P1, False),
             (63.4, P3, False), (54.0, P3, False), (40.2, P3, False), (6.1, INK, False)]


def fig3(lang):
    t = F3[lang]
    ax = 330 if lang == "zh" else 340
    unit = 7.0
    out = [txt(40, 58, t["title"], 26, weight="600")]
    y = 112
    for name, (v, c, approx) in zip(t["rows"], F3_VALUES):
        out.append(txt(40, y + 26, name, 20))
        out.append(rect(ax, y, v * unit, 36, c, ".92" if c == INK else "1"))
        label = ("%s%g%%" % (t["approx"], v)) if approx else "%.1f%%" % v
        out.append(txt(ax + v * unit + 10, y + 26, label, 19))
        y += 80
    out.append(line(ax, 98, ax, y - 30))
    out += [txt(40, y + 10, t["foot"][0], 16, op=".75"),
            txt(40, y + 36, t["foot"][1], 16, op=".75")]
    return svg(1080, y + 60, t["title"], out)


if __name__ == "__main__":
    for lang in ("en", "zh"):
        d = os.path.join(ROOT, "_includes", "charts", "ai-capex", lang)
        os.makedirs(d, exist_ok=True)
        for name, fn in (("fig1.svg", fig1), ("fig2.svg", fig2), ("fig3.svg", fig3)):
            path = os.path.join(d, name)
            open(path, "w", encoding="utf-8").write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))
