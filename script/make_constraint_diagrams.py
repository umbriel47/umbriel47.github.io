#!/usr/bin/env python3
"""Generate the three diagrams for the biology-conservation-laws post as SVG.

    python3 script/make_constraint_diagrams.py

The WeChat originals are rasters with Chinese labels burnt in. Redrawn for the
same reasons as script/make_charts.py: the English post needs its own labels,
and inlined via {% include %} text and outlines are currentColor and follow the
site's light/dark toggle. The accent is fixed; accent text carries
.accent-text so style.css can lighten it on the dark theme, and shapes that
were white or near-black in the original use the page's --bg / ink so they
invert with it. The figures keep their captions in the post, so they draw no
title of their own.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCENT = "#5b4fc4"
BG = "var(--bg, #fff)"          # the page background, for "paper-coloured" fills
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")

T = {
    "zh": {
        "f1_desc": "机制与约束的区别：左侧是规定步骤与方向的有向流程，右侧是从可能的解集中"
                   "削去大部分、只留下一小块可达状态的边界",
        "mechanism": "机制", "constraint": "约束",
        "flow": ["DNA", "RNA", "蛋白质"], "flow_note": "规定步骤与方向",
        "space": "可能的解集", "reachable": "仍可达的状态", "cut_note": "削减可达范围",
        "f2_desc": "守恒约束对预测空间的压缩：几条守恒关系把大片未受约束的可能状态切成一条窄带，"
                   "实验观测落在窄带之内",
        "unconstrained": "未受约束的可能状态", "conservation": "守恒约束",
        "allowed": "允许状态", "observed": "实验观测",
        "stronger": "约束越强，允许区域越窄",
        "x": "状态变量 1", "y": "状态变量 2",
        "f3_desc": "生物学中候选约束的三个来源：物理约束、量上的不变量和标度关系，"
                   "汇总后要回答哪些是真约束、哪些只是拟合",
        "cols": [("物理约束", ["能量", "扩散", "温度"]),
                 ("量上的不变量", ["化学计量", "序列保守"]),
                 ("标度关系", [])],
        "extrapolate": "能否跨类群外推？",
        "question": "哪些是真约束，哪些只是拟合",
    },
    "en": {
        "f1_desc": "Mechanism versus constraint: on the left, a directed flow that fixes the "
                   "steps and the direction; on the right, a boundary that cuts most of the "
                   "possible solutions away, leaving only a small reachable region",
        "mechanism": "Mechanism", "constraint": "Constraint",
        "flow": ["DNA", "RNA", "Protein"], "flow_note": "Fixes the steps and the direction",
        "space": "Possible solutions", "reachable": ["States still", "reachable"],
        "cut_note": "Cuts down what can be reached",
        "f2_desc": "How conservation constraints compress the prediction space: a few "
                   "conservation relations cut a large space of unconstrained possible states "
                   "down to a narrow band, and experimental observations fall inside it",
        "unconstrained": "Unconstrained possible states", "conservation": "Conservation constraint",
        "allowed": "Allowed states", "observed": "Experimental observation",
        "stronger": ["The stronger the constraint,", "the narrower the allowed region"],
        "x": "State variable 1", "y": "State variable 2",
        "f3_desc": "Three sources of candidate constraints in biology: physical constraints, "
                   "quantitative invariants and scaling relations; together they raise the "
                   "question of which are real constraints and which are only fits",
        "cols": [("Physical constraints", ["Energy", "Diffusion", "Temperature"]),
                 ("Quantitative invariants", ["Stoichiometry", "Sequence conservation"]),
                 ("Scaling relations", [])],
        "extrapolate": "Extrapolates across taxa?",
        "question": "Which are real constraints, and which are only fits?",
    },
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=22, anchor="middle", weight="400", fill="currentColor", op="1",
        extra=""):
    cls = ' class="accent-text"' if fill == ACCENT else ""
    if fill.startswith("var("):
        paint = ' style="fill: %s"' % fill
    else:
        paint = ' fill="%s" fill-opacity="%s"' % (fill, op)
    return ('  <text%s x="%d" y="%d" font-size="%d" text-anchor="%s" font-weight="%s"%s%s>'
            '%s</text>' % (cls, x, y, size, anchor, weight, paint, extra, esc(s)))


def lines(cx, cy, rows, size=22, gap=28, **kw):
    if isinstance(rows, str):
        rows = [rows]
    y0 = cy - (len(rows) - 1) * gap / 2 + size * .35
    return [txt(cx, y0 + i * gap, r, size, **kw) for i, r in enumerate(rows)]


def box(x, y, w, h, stroke=ACCENT, sop="1", fill="none", fop="1", sw=3, rx=14):
    paint = ('style="fill: %s"' % fill if fill.startswith("var(")
             else 'fill="%s" fill-opacity="%s"' % (fill, fop))
    return ('  <rect x="%d" y="%d" width="%d" height="%d" rx="%d" %s stroke="%s" '
            'stroke-opacity="%s" stroke-width="%s"/>' % (x, y, w, h, rx, paint, stroke,
                                                          sop, sw))


def seg(x1, y1, x2, y2, stroke="currentColor", op="1", w=3, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, stroke, op, w, d))


def head(x, y, angle_deg, fill="currentColor", size=18):
    """Arrowhead with its tip at (x, y), pointing along angle_deg (0 = right)."""
    return ('  <path d="M0 0 L%d %d L%d %d Z" fill="%s" transform="translate(%d %d) '
            'rotate(%d)"/>' % (-size, -size * .55, -size, size * .55, fill, x, y, angle_deg))


def svg(w, h, desc, body):
    return ('<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n'
            % (w, h, esc(desc), FONT, esc(desc), "\n".join(body)))


def mechanism_vs_constraint(lang):
    t = T[lang]
    out = [txt(270, 110, t["mechanism"], 34, weight="700"),
           txt(810, 110, t["constraint"], 34, weight="700"),
           seg(540, 50, 540, 570, ACCENT, ".6", 2.5, "8 8")]
    # mechanism: DNA → RNA → protein
    xs = (30, 210, 390)
    for i, (x, name) in enumerate(zip(xs, t["flow"])):
        last = i == 2
        out.append(box(x, 270, 120, 84, fill=ACCENT if last else BG))
        out += lines(x + 60, 312, name, 26, weight="700",
                     fill="#fff" if last else "currentColor")
        if i:
            out += [seg(x - 56, 312, x - 18, 312), head(x - 4, 312, 0, size=22)]
    out.append(txt(270, 430, t["flow_note"], 24))
    # constraint: the possible space, cut down to a small reachable region
    out += ['  <ellipse cx="810" cy="320" rx="230" ry="170" fill="%s" fill-opacity=".18" '
            'stroke="%s" stroke-opacity=".55" stroke-width="3"/>' % (ACCENT, ACCENT),
            txt(810, 222, t["space"], 24),
            seg(640, 300, 762, 346, ACCENT, "1", 3.5), head(782, 354, 21, ACCENT, 24),
            box(790, 320, 190, 86, fill=BG, sw=4, rx=12)]
    out += lines(885, 363, t["reachable"], 22, 26, weight="700", fill=ACCENT)
    out.append(txt(810, 545, t["cut_note"], 24))
    return svg(1080, 620, t["f1_desc"], out)


def compression(lang):
    t = T[lang]
    out = [
        # axes
        seg(130, 620, 130, 52, w=3), head(130, 42, -90, size=20),
        seg(130, 620, 1020, 620, w=3), head(1030, 620, 0, size=20),
        txt(580, 680, t["x"], 24),
        txt(70, 335, t["y"], 24, extra=' transform="rotate(-90 70 335)"'),
        # the unconstrained space
        box(190, 90, 790, 480, ACCENT, ".55", ACCENT, ".07", 3, 28),
        txt(215, 145, t["unconstrained"], 24, "start"),
        txt(950, 133, t["conservation"], 26, "end", "700", ACCENT),
        # the allowed band
        '  <path d="M220 520 L800 157 L940 197 L360 560 Z" fill="%s" fill-opacity=".25"/>'
        % ACCENT,
        seg(220, 520, 800, 157, ACCENT, "1", 3.5),
        seg(290, 540, 870, 177, ACCENT, "1", 3.5),
        seg(360, 560, 940, 197, ACCENT, "1", 3.5),
        # labels
        txt(400, 255, t["allowed"], 24, weight="700"),
        seg(432, 270, 493, 357, w=2.5),
        '  <path d="M450 418 l7.6 15.4 17 2.5 -12.3 12 2.9 16.9 -15.2 -8 -15.2 8 '
        '2.9 -16.9 -12.3 -12 17 -2.5 z" fill="currentColor"/>',
        seg(466, 460, 520, 505, w=2.5),
    ]
    if lang == "zh":
        out += [txt(525, 535, t["observed"], 24, "start"),
                txt(820, 478, t["stronger"], 24, fill=ACCENT)]
        sy = 428
    else:
        out += [txt(525, 535, t["observed"], 24, "start")]
        out += lines(825, 462, t["stronger"], 21, 28, fill=ACCENT)
        sy = 420
    out += [seg(848, sy, 795, 305, ACCENT, "1", 3.5), head(786, 296, -115, ACCENT, 22)]
    return svg(1080, 720, t["f2_desc"], out)


def sources(lang):
    t = T[lang]
    out = []
    for i, (title, items) in enumerate(t["cols"]):
        x = 45 + i * 345
        out += [box(x, 40, 300, 320, ACCENT, ".55", BG, sw=3, rx=22),
                txt(x + 150, 100, title, 26 if lang == "zh" else 23, weight="700"),
                seg(x + 40, 125, x + 260, 125, ACCENT, ".55", 2)]
        y0 = 180 if len(items) == 3 else 205
        for j, item in enumerate(items):
            out.append(txt(x + 150, y0 + j * 60 + 8, item, 24 if lang == "zh" else 22))
    # the scaling-relation sketch
    out += [seg(790, 290, 980, 160, ACCENT, "1", 4)]
    for cx, cy in ((820, 262), (862, 247), (900, 212), (945, 196)):
        out.append('  <circle cx="%d" cy="%d" r="7" fill="%s" fill-opacity=".55"/>'
                   % (cx, cy, ACCENT))
    out.append(txt(885, 335, t["extrapolate"], 23 if lang == "zh" else 20, fill=ACCENT))
    # the three sources converge on one question
    out += [seg(195, 360, 195, 470, ACCENT), seg(540, 360, 540, 470, ACCENT),
            seg(193, 470, 785, 470, ACCENT), head(800, 470, 0, ACCENT, 26),
            seg(885, 360, 885, 400, ACCENT), head(885, 418, 90, ACCENT, 24),
            '  <rect x="805" y="418" width="160" height="104" rx="14" fill="currentColor"/>',
            txt(885, 486, "?", 44, weight="700", fill=BG)]
    if lang == "zh":
        out.append(txt(440, 528, t["question"], 25))
    else:
        out.append(txt(440, 528, t["question"], 22))
    return svg(1080, 580, t["f3_desc"], out)


if __name__ == "__main__":
    for lang in T:
        d = os.path.join(ROOT, "_includes", "charts", "biology-constraints", lang)
        os.makedirs(d, exist_ok=True)
        for name, fn in (("fig1.svg", mechanism_vs_constraint), ("fig2.svg", compression),
                         ("fig3.svg", sources)):
            path = os.path.join(d, name)
            open(path, "w", encoding="utf-8").write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))
