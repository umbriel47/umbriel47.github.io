#!/usr/bin/env python3
"""Generate the two diagrams for the consciousness-and-reality post as SVG.

    python3 script/make_mind_diagrams.py

The WeChat originals are rasters with Chinese labels burnt in. Redrawn for the
same reasons as script/make_charts.py: the English post needs its own labels,
and inlined via {% include %} text and outlines are currentColor and follow the
site's light/dark toggle. The accent is fixed; accent text carries
.accent-text so style.css can lighten it on the dark theme, and white boxes
use the page's --bg so they invert with it. Figures keep their captions in the
post, so they draw no title of their own. (The article's third figure is a
table drawn as an image; the post renders it as a real table instead.)
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCENT = "#5b4fc4"
MID = "#8b80e6"
BG = "var(--bg, #fff)"
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")

T = {
    "zh": {
        "f1_desc": "两种「双层」实在图景：Laszlo 以不可观测的 A 维度承载显现的 M 维度；"
                   "Glattfelder（2019）以信息为基底，物理结构与主观体验是它的外在与内在两面",
        "laszlo_sub": "阿卡夏范式（2004–2016）",
        "m_head": "M 维度：显现的世界", "m_sub": ["粒子、星系、生命、大脑"],
        "a_head": "A 维度：阿卡夏", "a_sub": ["不可观测的深层信息场", "（被等同于量子真空）"],
        "arrow": ["显现", "与「记忆」"],
        "glatt_sub": "信息本体论（2019）",
        "outer": ("外在一面", "物理结构"), "inner": ("内在一面", "主观体验"),
        "info": "信息", "info_sub": "「只有信息存在」",
        "f2_desc": "意识在实在中的位置：从物理主义到观念论的谱系，以及 Laszlo、Glattfelder 和 "
                   "Kastrup 的大致位置；每类立场下方标注它需要支付的主要解释代价",
        "q": "什么是最基本的？", "matter": "物质", "mind": "心智 / 意识",
        "positions": ["物理主义", "双面一元论", "泛心论", "观念论"],
        "g2019": "Glattfelder 2019", "g2025": "Glattfelder 2025",
        "kastrup": "Kastrup 分析观念论", "laszlo": "Laszlo 后期",
        "price": "各自需要支付的解释代价",
        "costs": [["主观体验", "从何而来"], ["「两面」为何", "恰好对应"],
                  ["组合问题：", "微体验如何成「我」"], ["解组合问题；", "物理规律为何稳定"]],
        "cost_size": 20,
    },
    "en": {
        "f1_desc": "Two two-layer pictures of reality: Laszlo's unobservable A dimension "
                   "underlies the manifest M dimension; Glattfelder (2019) takes information "
                   "as the base, with physical structure and subjective experience as its outer "
                   "and inner faces",
        "laszlo_sub": "Akashic paradigm (2004–2016)",
        "m_head": "M dimension: the manifest world",
        "m_sub": ["Particles, galaxies, life, brains"],
        "a_head": "A dimension: the Akasha",
        "a_sub": ["An unobservable, deep information field", "(equated with the quantum vacuum)"],
        "arrow": ["Manifestation", "and “memory”"],
        "glatt_sub": "Information ontology (2019)",
        "outer": ("Outer face", "Physical structure"),
        "inner": ("Inner face", "Subjective experience"),
        "info": "Information", "info_sub": "“Only information exists”",
        "f2_desc": "Where consciousness sits in reality: the spectrum from physicalism to "
                   "idealism, with the rough positions of Laszlo, Glattfelder and Kastrup, and "
                   "under each position the main explanatory price it has to pay",
        "q": "What is most fundamental?", "matter": "Matter", "mind": "Mind / consciousness",
        "positions": ["Physicalism", "Dual-aspect monism", "Panpsychism", "Idealism"],
        "g2019": "Glattfelder 2019", "g2025": "Glattfelder 2025",
        "kastrup": "Kastrup's analytic idealism", "laszlo": "Laszlo (later work)",
        "price": "The explanatory price each must pay",
        "costs": [["Where does subjective", "experience come from?"],
                  ["Why do the two faces", "correspond so neatly?"],
                  ["Combination problem: how", "do micro-experiences", "make an “I”?"],
                  ["Decombination problem;", "why are physical laws", "so stable?"]],
        "cost_size": 16,
    },
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=22, anchor="middle", weight="400", fill="currentColor", op="1"):
    cls = ' class="accent-text"' if fill == ACCENT else ""
    paint = (' style="fill: %s"' % fill if fill.startswith("var(")
             else ' fill="%s" fill-opacity="%s"' % (fill, op))
    return ('  <text%s x="%d" y="%d" font-size="%d" text-anchor="%s" font-weight="%s"%s>'
            '%s</text>' % (cls, x, y, size, anchor, weight, paint, esc(s)))


def lines(cx, cy, rows, size=22, gap=28, **kw):
    y0 = cy - (len(rows) - 1) * gap / 2 + size * .35
    return [txt(cx, y0 + i * gap, r, size, **kw) for i, r in enumerate(rows)]


def box(x, y, w, h, stroke=ACCENT, sop="1", fill=BG, fop="1", sw=3, rx=14, dash=""):
    paint = ('style="fill: %s"' % fill if fill.startswith("var(")
             else 'fill="%s" fill-opacity="%s"' % (fill, fop))
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('  <rect x="%d" y="%d" width="%d" height="%d" rx="%d" %s stroke="%s" '
            'stroke-opacity="%s" stroke-width="%s"%s/>' % (x, y, w, h, rx, paint, stroke,
                                                            sop, sw, d))


def seg(x1, y1, x2, y2, stroke=ACCENT, op="1", w=3, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, stroke, op, w, d))


def head(x, y, angle, fill=ACCENT, size=22):
    return ('  <path d="M0 0 L%d %d L%d %d Z" fill="%s" transform="translate(%d %d) '
            'rotate(%d)"/>' % (-size, -size * .55, -size, size * .55, fill, x, y, angle))


def svg(w, h, desc, body):
    return ('<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n'
            % (w, h, esc(desc), FONT, esc(desc), "\n".join(body)))


def two_pictures(lang):
    t = T[lang]
    en = lang == "en"
    out = [seg(540, 40, 540, 660, ACCENT, ".55", 2.5, "8 8"),
           # Laszlo
           txt(270, 78, "Laszlo", 36, weight="700"),
           txt(270, 114, t["laszlo_sub"], 21, fill=ACCENT),
           box(60, 160, 420, 150),
           txt(270, 220, t["m_head"], 23 if en else 28, weight="700")]
    out += lines(270, 255, t["m_sub"], 20)
    out += [seg(230, 430, 230, 330), head(230, 312, -90),
            seg(310, 322, 310, 422), head(310, 440, 90)]
    out += lines(330 if not en else 328, 376, t["arrow"], 20, 30, anchor="start")
    out += [box(60, 440, 420, 170, fill=ACCENT, sw=0, rx=14),
            txt(270, 503, t["a_head"], 25 if en else 28, weight="700", fill="#fff")]
    out += lines(270, 555, t["a_sub"], 18 if en else 20, 30, fill="#fff")
    # Glattfelder
    out += [txt(810, 78, "Glattfelder", 36, weight="700"),
            txt(810, 114, t["glatt_sub"], 21, fill=ACCENT)]
    for x, (h, s) in ((600, t["outer"]), (830, t["inner"])):
        out += [box(x, 160, 190, 150),
                txt(x + 95, 220, h, 23 if en else 26, weight="700"),
                txt(x + 95, 262, s, 17 if en else 20)]
    out += [seg(740, 430, 698, 330), head(690, 312, -112),
            seg(880, 430, 918, 330), head(925, 312, -69),
            box(600, 440, 420, 170, fill=ACCENT, sw=0, rx=14),
            txt(810, 513, t["info"], 30, weight="700", fill="#fff"),
            txt(810, 560, t["info_sub"], 21, fill="#fff")]
    return svg(1080, 700, t["f1_desc"], out)


def spectrum(lang):
    t = T[lang]
    en = lang == "en"
    xs = (150, 390, 620, 900)
    out = [txt(540, 60, t["q"], 27, weight="700"),
           txt(70, 140, t["matter"], 22, "start", "700"),
           txt(1010, 140, t["mind"], 22, "end", "700"),
           seg(60, 250, 990, 250, "currentColor", "1", 3),
           head(70, 250, 0, "currentColor", 30), head(1012, 250, 0, "currentColor", 30)]
    dots = ("currentColor", MID, MID, ACCENT)
    for x, name, c in zip(xs, t["positions"], dots):
        out += [txt(x, 207, name, 21 if en else 24, weight="700"),
                '  <circle cx="%d" cy="250" r="16" fill="%s"/>' % (x, c)]

    def pill(cx, cy, label, w=260):
        return [box(cx - w // 2, cy - 28, w, 56, rx=28, sw=3),
                txt(cx, cy + 7, label, 18 if en else 20, weight="700", fill=ACCENT)]
    out += pill(390, 318, t["g2019"], 180 if not en else 190)
    out += [seg(485, 318, 740, 318, ACCENT, "1", 3, "8 8"), head(764, 318, 0)]
    out += pill(900, 318, t["g2025"])
    out += pill(900, 386, t["kastrup"])
    out += pill(900, 454, t["laszlo"])
    out.append(txt(540, 558, t["price"], 22, weight="700"))
    for i, rows in enumerate(t["costs"]):
        x = 60 + i * 240
        out.append(box(x, 590, 220, 90, ACCENT, ".5", sw=2.5, rx=12))
        gap = 26 if len(rows) == 2 and not en else 21
        out += lines(x + 110, 635, rows, t["cost_size"], gap)
    return svg(1080, 720, t["f2_desc"], out)


if __name__ == "__main__":
    for lang in T:
        d = os.path.join(ROOT, "_includes", "charts", "consciousness", lang)
        os.makedirs(d, exist_ok=True)
        for name, fn in (("fig1.svg", two_pictures), ("fig2.svg", spectrum)):
            path = os.path.join(d, name)
            open(path, "w", encoding="utf-8").write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))
