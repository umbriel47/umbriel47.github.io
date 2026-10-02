#!/usr/bin/env python3
"""Generate the two diagrams for the lab-automation post as inline SVG.

    python3 script/make_lab_diagrams.py

The WeChat originals are rasters with Chinese labels burnt in. Redrawn for the
same reasons as script/make_charts.py: the English post needs its own labels,
and inlined via {% include %} the text and outlines are currentColor and follow
the site's light/dark toggle. Only the accent is a fixed colour, and accent
text is lightened on the dark theme by the .accent-text rule in style.css.

These figures carry captions in the post (the originals had real captions, not
a repeat of an in-image title), so the SVGs draw no title of their own.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCENT = "#5b4fc4"
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")

T = {
    "zh": {
        "f1_desc": "编码是有损转译：操作步骤进入标准化流程，异常感知与情境判断留在漏斗之外",
        "manual": "手工流程",
        "manual_items": ["操作步骤", "感觉反馈", "情境线索", "异常信号"],
        "funnel": ["编码进", "协议与数据"],
        "standard": "标准化流程",
        "standard_items": ["协议步骤", "仪器读数", "质控参数"],
        "left_out": "未被编码：异常感知、情境判断",
        "f2_desc": "两条反馈回路：手工流程中异常进入人的判断并修正方法；"
                   "自动化流程中异常被记为噪声或重跑，回路不经过判断",
        "loop1": "手工流程回路",
        "loop1_steps": [["出现异常"], ["人察觉"], ["判断真假异常"], ["修正方法"]],
        "loop1_foot": "纠错能力被反复训练",
        "loop2": "自动化流程回路",
        "loop2_steps": [["出现异常"], ["记为噪声", "或直接重跑"], ["无记录"], ["回到起点"]],
        "loop2_foot": "纠错机会不再出现",
    },
    "en": {
        "f1_desc": "Encoding is a lossy translation: operating steps enter the "
                   "standardised process, while sensing anomalies and judging "
                   "context stay outside the funnel",
        "manual": "Manual process",
        "manual_items": ["Operating steps", "Sensory feedback", "Contextual cues",
                         "Anomaly signals"],
        "funnel": ["Encoded into", "protocols & data"],
        "standard": "Standardised process",
        "standard_items": ["Protocol steps", "Instrument readings", "QC parameters"],
        "left_out": "Not encoded: sensing anomalies, judging context",
        "f2_desc": "Two feedback loops: in the manual process an anomaly reaches "
                   "human judgment and corrects the method; in the automated "
                   "process it is logged as noise or rerun, and the loop never "
                   "passes through judgment",
        "loop1": "Manual loop",
        "loop1_steps": [["Anomaly occurs"], ["A person", "notices"],
                        ["Real or", "spurious?"], ["Method", "corrected"]],
        "loop1_foot": "The ability to correct errors is trained again and again",
        "loop2": "Automated loop",
        "loop2_steps": [["Anomaly occurs"], ["Logged as noise", "or simply rerun"],
                        ["No record"], ["Back to start"]],
        "loop2_foot": "The chance to correct errors no longer arises",
    },
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=17, anchor="middle", weight="400", fill="currentColor", op="1"):
    # Accent-coloured text is too dark on the dark theme; the class lets
    # style.css lighten it there (CSS overrides the fill attribute).
    cls = ' class="accent-text"' if fill == ACCENT else ""
    return ('  <text%s x="%d" y="%d" font-size="%d" text-anchor="%s" font-weight="%s" '
            'fill="%s" fill-opacity="%s">%s</text>'
            % (cls, x, y, size, anchor, weight, fill, op, esc(s)))


def lines(cx, cy, rows, size=17, gap=24, **kw):
    """Vertically centred multi-line label."""
    y0 = cy - (len(rows) - 1) * gap / 2 + size * .35
    return [txt(cx, y0 + i * gap, r, size, **kw) for i, r in enumerate(rows)]


def box(x, y, w, h, stroke="currentColor", sop=".85", fill="none", fop="0",
        sw=2, rx=14, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('  <rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" '
            'fill-opacity="%s" stroke="%s" stroke-opacity="%s" stroke-width="%s"%s/>'
            % (x, y, w, h, rx, fill, fop, stroke, sop, sw, d))


def seg(x1, y1, x2, y2, stroke="currentColor", op=".85", w=2):
    return ('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity="%s" '
            'stroke-width="%s"/>' % (x1, y1, x2, y2, stroke, op, w))


def svg(w, h, desc, body):
    return ('<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n'
            % (w, h, esc(desc), FONT, esc(desc), "\n".join(body)))


def funnel(lang):
    t = T[lang]
    out = []
    # manual process (accent outline; the tacit items in accent colour)
    out += [box(40, 80, 300, 380, ACCENT, "1"),
            txt(190, 140, t["manual"], 24, weight="600"),
            seg(80, 165, 300, 165, ACCENT, ".5", 1.5)]
    for i, item in enumerate(t["manual_items"]):
        out.append(txt(190, 214 + i * 65, item, 19,
                       fill="currentColor" if i == 0 else ACCENT))
    # funnel
    out += [seg(345, 270, 392, 270),
            '  <path d="M400 110 H680 L580 330 V420 H500 V330 Z" fill="%s"/>' % ACCENT]
    out += lines(540, 202, t["funnel"], 20, 34, fill="#fff",
                 weight="500")
    out.append(seg(615, 270, 732, 270))
    # standardised process
    out += [box(740, 80, 300, 380),
            txt(890, 140, t["standard"], 24, weight="600"),
            seg(780, 165, 1000, 165, ACCENT, ".5", 1.5)]
    for i, item in enumerate(t["standard_items"]):
        out.append(txt(890, 244 + i * 65, item, 19))
    # what falls out of the funnel
    for x2 in (450, 540, 630):
        out.append(seg(540 + (x2 - 540) // 3, 425, x2, 528, ACCENT, ".55", 2))
    out += [box(270, 540, 540, 110, ACCENT, ".55"),
            txt(540, 604, t["left_out"], 20)]
    return svg(1080, 690, t["f1_desc"], out)


def loops(lang):
    t = T[lang]
    out = []
    bw, bh, xs = 210, 90, (45, 305, 565, 825)

    def row(y, title, steps, foot, manual):
        r = [txt(45, y - 34, title, 22, "start", "500",
                 ACCENT if manual else "currentColor")]
        for i, (x, step) in enumerate(zip(xs, steps)):
            if i:
                r.append(seg(x - 47, y + bh // 2, x - 3, y + bh // 2,
                             ACCENT if manual else "currentColor"))
            if manual and i == 3:                      # the step that closes the loop
                r += [box(x, y, bw, bh, ACCENT, "1", ACCENT, "1")]
                r += lines(x + bw // 2, y + bh // 2, step, 19, fill="#fff", weight="500")
            elif not manual and i == 2:                # "no record": faded, dashed
                r += [box(x, y, bw, bh, ACCENT, ".45", dash="6 5")]
                r += lines(x + bw // 2, y + bh // 2, step, 19, fill=ACCENT, op=".6")
            else:
                r += [box(x, y, bw, bh, ACCENT if manual else "currentColor",
                          "1" if manual else ".85", ACCENT, ".07")]
                r += lines(x + bw // 2, y + bh // 2, step, 19)
        # return path under the row, from the last box back to the first
        c = ACCENT if manual else "currentColor"
        b = y + bh + 50
        r += ['  <path d="M%d %d V%d H%d V%d" fill="none" stroke="%s" stroke-width="2"/>'
              % (xs[3] + bw // 2, y + bh, b, xs[0] + bw // 2, y + bh, c),
              txt(540, b + 48, foot, 21, weight="500",
                  fill=ACCENT if manual else "currentColor")]
        return r

    out += row(100, t["loop1"], t["loop1_steps"], t["loop1_foot"], True)
    out.append(seg(45, 360, 1035, 360, ACCENT, ".4", 1.5))
    out += row(460, t["loop2"], t["loop2_steps"], t["loop2_foot"], False)
    return svg(1080, 700, t["f2_desc"], out)


if __name__ == "__main__":
    for lang in T:
        d = os.path.join(ROOT, "_includes", "charts", "lab-anomalies", lang)
        os.makedirs(d, exist_ok=True)
        for name, fn in (("fig1.svg", funnel), ("fig2.svg", loops)):
            path = os.path.join(d, name)
            open(path, "w", encoding="utf-8").write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))
