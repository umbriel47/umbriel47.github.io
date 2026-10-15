#!/usr/bin/env python3
"""Generate the five figures for the belief-flow pricing post as SVG, both languages.

    python3 script/make_belief_flow_charts.py

The WeChat originals are rasters with Chinese labels burnt in; these are rebuilt
for the same reasons as script/make_charts.py. Text and axes are currentColor and
follow the light/dark toggle; purple text carries .accent-text so style.css can
lighten it on the dark theme; white boxes use the page's --bg.

Figures 3 and 4 are not traced from the images; they are recomputed from the
models the article states.

  Figure 3: projects with a 20% prior of being effective, 6 years of development
  at 1 unit a year, 40 units on success; the efficacy signal is Brownian, the
  drifts of effective and ineffective projects differ by 1, noise 1.2 a year.
  For each review interval the optimal stopping rule was solved by backward
  induction on a log-odds grid (Gauss-Hermite quadrature over each interval's
  likelihood-ratio increment). The values below are that solution, rounded to
  0.01; they reproduce every number the text quotes (never stopping 2.0,
  near-continuous 3.15, yearly 3.01, two-yearly 2.85-2.86, weekly with a 0.02
  review cost 0.37, readouts-only aligned 2.86 and misaligned 2.4-2.5).

  Figure 4: the originator's value-growth rate r1(t) = c + b(e^{-kt} - e^{-3k}),
  the acquirer's a constant c, so the curves cross at the optimal transfer time
  t = 3. k and b are fixed by the losses the text gives for transferring at
  year 2 (0.16) and year 4 (0.10); with c = 1 the curves also match the
  proportions of the original figure.

Figure 2's belief path is illustrative, as in the original: a seeded random path
pinned to the same events (crossing the escalation boundary at 1.5 years, jumps
at the readouts in years 2 and 4, crossing the stop boundary at about 4.1).
"""
import math
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P1, P2, P3 = "#5b4fc4", "#8b80e6", "#b3abf0"
INK = "currentColor"
BG = "var(--bg, #fff)"
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=18, anchor="start", weight="400", fill=INK, op="1", extra=""):
    cls = ' class="accent-text"' if fill == P1 else ""
    paint = (' style="fill: %s"' % fill if fill.startswith("var(")
             else ' fill="%s" fill-opacity="%s"' % (fill, op))
    return ('  <text%s x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" font-weight="%s"%s%s>'
            '%s</text>' % (cls, x, y, size, anchor, weight, paint, extra, esc(s)))


HALO = ' style="paint-order: stroke; stroke: var(--bg, #fff); stroke-width: 5px"'


def rich(x, y, parts, size=17, anchor="start", halo=False):
    """One line made of (text, weight, fill) runs. A halo in the page colour keeps a
    label readable where it crosses a line."""
    spans = "".join('<tspan font-weight="%s"%s>%s</tspan>'
                    % (w, ' class="accent-text" fill="%s"' % f if f == P1
                       else ' fill="%s"' % f, esc(t)) for t, w, f in parts)
    return '  <text x="%.1f" y="%.1f" font-size="%d" text-anchor="%s"%s>%s</text>' % (
        x, y, size, anchor, HALO if halo else "", spans)


def rect(x, y, w, h, fill, op="1", rx=0, stroke="", sw=0):
    paint = ('style="fill: %s"' % fill if fill.startswith("var(")
             else 'fill="%s" fill-opacity="%s"' % (fill, op))
    st = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ""
    return '  <rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" %s%s/>' % (
        x, y, max(w, 0), h, rx, paint, st)


def line(x1, y1, x2, y2, stroke=INK, op="1", w=1.5, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, stroke, op, w, d))


def path(points, stroke=P1, w=3, dash="", op="1"):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    pts = " ".join("%.1f,%.1f" % p for p in points)
    return ('  <polyline points="%s" fill="none" stroke="%s" stroke-opacity="%s" '
            'stroke-width="%s" stroke-linejoin="round"%s/>' % (pts, stroke, op, w, d))


def dot(x, y, r, fill):
    paint = 'style="fill: %s"' % fill if fill.startswith("var(") else 'fill="%s"' % fill
    return '  <circle cx="%.1f" cy="%.1f" r="%s" %s/>' % (x, y, r, paint)


def diamond(x, y, r=10, fill=INK):
    return '  <path d="M%.1f %.1f l%d %d l-%d %d l-%d -%d z" fill="%s"/>' % (
        x, y - r, r, r, r, r, r, r, fill)


def head(x, y, angle, fill=INK, size=14):
    return ('  <path d="M0 0 L%d %d L%d %d Z" fill="%s" transform="translate(%.1f %.1f) '
            'rotate(%d)"/>' % (-size, -size * .55, -size, size * .55, fill, x, y, angle))


def svg(w, h, desc, body):
    return ('<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n'
            % (w, h, esc(desc), FONT, esc(desc), "\n".join(body)))


def L(lang, zh, en):
    return zh if lang == "zh" else en


# ------------------------------------------------------------ figure 1: four lineages

F1_COLS = [
    (("统计决策与序贯分析", "Statistical decisions & sequential analysis"), [
        (1933, "Thompson 抽样", "Thompson sampling"),
        (1945, "Wald 序贯检验", "Wald sequential test"),
        (1950, "Wald 统计决策函数", "Wald decision functions"),
        (1961, "Raiffa–Schlaifer", "Raiffa–Schlaifer"),
        (1966, "Howard 信息价值", "Howard value of info"),
        (1970, "DeGroot 最优决策", "DeGroot optimal decisions")]),
    (("动态规划与最优停止", "Dynamic programming & optimal stopping"), [
        (1957, "Bellman 动态规划", "Bellman dynamic programming"),
        (1963, "Shiryaev 最快检测", "Shiryaev quickest detection"),
        (1965, "Åström 信念状态", "Åström belief state"),
        (1973, "Smallwood–Sondik", "Smallwood–Sondik"),
        (1979, "Gittins 指数", "Gittins index"),
        (2001, "Moscarini–Smith", "Moscarini–Smith"),
        (2005, "Keller–Rady–Cripps", "Keller–Rady–Cripps")]),
    (("实物期权与资产定价", "Real options & asset pricing"), [
        (1973, "Black–Scholes 定价", "Black–Scholes pricing"),
        (1977, "Myers 实物期权", "Myers real options"),
        (1979, "Geske 复合期权", "Geske compound options"),
        (1986, "McDonald–Siegel", "McDonald–Siegel"),
        (1989, "Dixit 不行动区间", "Dixit inaction band"),
        (1994, "Dixit–Pindyck", "Dixit–Pindyck"),
        (2003, "Pástor–Veronesi", "Pástor–Veronesi")]),
    (("临床试验设计与监管", "Clinical trial design & regulation"), [
        (1969, "Armitage 重复检验", "Armitage repeated tests"),
        (1977, "Pocock 成组序贯", "Pocock group sequential"),
        (1979, "O'Brien–Fleming", "O'Brien–Fleming"),
        (1983, "Lan–DeMets 消耗函数", "Lan–DeMets spending"),
        (2009, "I-SPY 2 平台试验", "I-SPY 2 platform trial"),
        (2019, "FDA 适应性设计", "FDA adaptive design"),
        (2026, "FDA 贝叶斯草案", "FDA Bayesian draft")]),
]
F1_DESC = ("与本文相关的四条理论脉络：统计决策与序贯分析、动态规划与最优停止、实物期权与资产定价、临床试验设计与监管",
           "Four lines of theory behind this piece: statistical decisions and sequential "
           "analysis, dynamic programming and optimal stopping, real options and asset "
           "pricing, and clinical trial design and regulation")


def fig1(lang):
    zh = lang == "zh"
    y_of = lambda yr: 150 + (yr - 1930) * 10.4
    out = []
    for yr in range(1930, 2031, 10):
        out += [line(90, y_of(yr), 1060, y_of(yr), op=".1", w=1),
                txt(70, y_of(yr) + 6, yr, 18, "end", op=".5")]
    for c, (head_, events) in enumerate(F1_COLS):
        x = 118 + c * 240
        out.append(rect(x - 18, 40, 220, 70, P1, ".1", rx=10))
        if zh:
            out.append(txt(x + 92, 84, head_[0], 21, "middle", "700"))
        else:
            words = head_[1].split(" & ")
            out += [txt(x + 92, 70, words[0] + " &", 15, "middle", "700"),
                    txt(x + 92, 92, words[1], 15, "middle", "700")]
        out.append(line(x, 150, x, 1190, P3, "1", 2))
        prev_y = -99
        for yr, z, e in events:
            y = y_of(yr)
            ly = y if y - prev_y > 22 else prev_y + 24        # nudge labels that would collide
            accent = yr >= 2009
            fill = P1 if accent else INK
            out.append(dot(x, y, 7, fill))
            if ly != y:
                out.append(line(x + 6, y + 4, x + 16, ly - 2, op=".4", w=1))
            out.append(rich(x + 18, ly + 6, [(str(yr) + " ", "700", fill),
                                              (z if zh else e, "400", fill)],
                            18 if zh else 15, halo=True))
            prev_y = ly
    return svg(1080, 1230, L(lang, *F1_DESC), out)


# ------------------------------------------------------------ figure 2: three continuities

UP, LO = 0.62, 0.22


def belief_path():
    """Seeded, pinned random path for the illustrative belief trajectory."""
    anchors = [(0, .37), (.25, .38), (.45, .52), (.75, .45), (1.0, .38), (1.2, .52),
               (1.5, UP), (1.65, .69), (1.98, .64), (2.0, .44), (2.3, .5), (2.55, .62),
               (2.8, .72), (3.1, .66), (3.5, .57), (3.95, .44), (4.0, .27), (4.1, LO),
               (4.4, .27), (4.75, .43), (5.0, .5), (5.2, .42), (5.45, .3), (5.6, .14),
               (6.0, .1)]
    rnd = random.Random(7)
    pts = []
    for (t0, p0), (t1, p1) in zip(anchors, anchors[1:]):
        n = max(2, int((t1 - t0) / 0.02))
        if t1 - t0 < 0.05:                        # a readout jump: straight drop
            pts.append((t1, p1))
            continue
        walk = [0.0]
        for _ in range(n):
            walk.append(walk[-1] + rnd.gauss(0, .022))
        for i in range(1, n + 1):
            f = i / n
            bridge = walk[i] - f * walk[-1]        # Brownian bridge: pinned at both anchors
            p = p0 + (p1 - p0) * f + bridge
            t = t0 + (t1 - t0) * f
            if t < 1.5:
                p = min(p, UP - .02)               # no crossing before the marked one
            if 2.0 < t < 4.0:
                p = max(p, LO + .06)
            pts.append((t, max(.03, min(.97, p))))
    return [(0, .37)] + pts


def fig2(lang):
    zh = lang == "zh"
    X = lambda t: 200 + t * 116.7
    Y = lambda p: 540 - p * 290
    out = []
    for y0, h, lab in ((60, 140, L(lang, "观测", "Observation")),
                       (230, 330, L(lang, "信念", "Belief")),
                       (590, 200, L(lang, "行动", "Action"))):
        out += [rect(30, y0, 150, h, P1, ".1", rx=12),
                txt(105, y0 + h / 2 + 10, lab, 28 if zh else 20, "middle", "700")]
    # observations
    rnd = random.Random(3)
    for _ in range(80):
        t = rnd.uniform(0.05, 5.95)
        h = rnd.uniform(14, 34)
        out.append(line(X(t), 170, X(t), 170 - h, P3, "1", 2.5))
    for t in (2, 4):
        out += [rect(X(t) - 3, 78, 6, 92, P1),
                txt(X(t) + 12, 96, L(lang, "读出", "Readout"), 20 if zh else 17, weight="700",
                    fill=P1)]
    out += [line(200, 170, 900, 170, w=2),
            txt(200, 195, L(lang, "入组、安全性、生物标志物、外部证据持续到达",
                            "Enrolment, safety, biomarkers and outside evidence keep arriving"),
                18 if zh else 16, op=".55")]
    # belief
    out += [rect(200, Y(UP), 700, Y(LO) - Y(UP), P1, ".08"),
            line(200, Y(UP), 900, Y(UP), P1, "1", 2, "8 6"),
            line(200, Y(LO), 900, Y(LO), P1, "1", 2, "8 6"),
            line(200, 250, 200, 540, w=2),
            txt(190, 258, "1", 16, "end", op=".5"), txt(190, 546, "0", 16, "end", op=".5"),
            txt(212, 274, L(lang, "后验成功概率 π(t)：随证据连续更新，读出时跳跃",
                            "Posterior probability of success π(t): updated continuously, "
                            "jumps at readouts"), 18 if zh else 15),
            txt(912, Y(UP) + 7, L(lang, "加码边界", "Escalate"), 20 if zh else 17, weight="700",
                fill=P1),
            txt(912, (Y(UP) + Y(LO)) / 2 + 7, L(lang, "不行动区间", "Inaction band"),
                19 if zh else 16, op=".5"),
            txt(912, Y(LO) + 7, L(lang, "终止边界", "Stop"), 20 if zh else 17, weight="700",
                fill=P1)]
    out.append(path([(X(t), Y(p)) for t, p in belief_path()], P1, 2.5))
    for t, p in ((1.5, UP), (4.1, LO)):
        out += [line(X(t), Y(p), X(t), 740, P1, ".8", 1.5, "3 4"),
                '  <circle cx="%.1f" cy="%.1f" r="8" style="fill: var(--bg, #fff)" stroke="%s" '
                'stroke-width="2.5"/>' % (X(t), Y(p), "currentColor")]
    # actions
    out += [txt(200, 621, L(lang, "阶段门：只在固定时点决策", "Stage gates: decide only at fixed dates"),
                20 if zh else 17, weight="700"),
            line(200, 650, 900, 650, op=".35", w=2)]
    out += [diamond(X(t), 650) for t in (0, 2, 4, 6)]
    out += [txt(200, 711, L(lang, "信念流决策：信念越过边界时触发评审",
                            "Belief-flow decisions: a review fires when belief crosses a boundary"),
                20 if zh else 17, weight="700", fill=P1),
            line(200, 740, 900, 740, P1, ".6", 2)]
    for t, lab in ((1.5, L(lang, "加码评审", "Escalation review")),
                   (4.1, L(lang, "终止评审", "Stop review"))):
        out += [dot(X(t), 740, 11, P1), txt(X(t) + 18, 774, lab, 19 if zh else 16, fill=P1)]
    # time axis
    out += [line(200, 810, 910, 810, w=2), head(922, 810, 0, size=18)]
    for t in range(7):
        out += [line(X(t), 810, X(t), 818, w=2), txt(X(t), 843, t, 17, "middle")]
    out.append(txt(940, 845, L(lang, "年", "years"), 18))
    return svg(1080, 870, L(lang, "三种连续性：观测、信念更新与行动", "Three kinds of continuity: "
                                  "observation, belief updating and action"), out)


# ------------------------------------------------------------ figure 3: review cadence

F3_X = [1 / 52, 2 / 52, 1 / 12, 1 / 6, 1 / 4, 1 / 2, 1, 1.5, 2, 3]       # review interval, years
F3_CONT = [3.15, 3.14, 3.14, 3.12, 3.11, 3.08, 3.01, 2.94, 2.86, 2.64]
F3_COST = [0.37, 1.46, 2.29, 2.68, 2.81, 2.93, 2.93, 2.88, 2.82, 2.61]
F3_READ = [2.86, 2.86, 2.86, 2.86, 2.86, 2.86, 2.86, 2.47, 2.86, 2.41]


def fig3(lang):
    zh = lang == "zh"
    X = lambda h: 140 + math.log(h * 52) * 170 * (860 / (math.log(156) * 170))
    Y = lambda v: 600 - v * 150
    out = []
    for v in range(4):
        out += [line(140, Y(v), 1000, Y(v), op=".1", w=1), txt(126, Y(v) + 6, v, 17, "end")]
    out += [line(140, Y(2), 1000, Y(2), op=".45", w=1.5, dash="2 4"),
            txt(1000, Y(2) + 28, L(lang, "从不终止：2.0", "Never stop: 2.0"), 17, "end", op=".5"),
            line(140, 600, 1000, 600, w=2)]
    ticks = [(1 / 52, "每周", "Weekly"), (1 / 12, "每月", "Monthly"), (1 / 4, "每季", "Quarterly"),
             (1 / 2, "半年", "6 months"), (1, "1 年", "1 yr"), (2, "2 年", "2 yrs"),
             (3, "3 年", "3 yrs")]
    for h, z, e in ticks:
        out += [line(X(h), 600, X(h), 608, w=2), txt(X(h), 634, z if zh else e, 17, "middle")]
    out.append(txt(570, 674, L(lang, "评审间隔（对数刻度）", "Review interval (log scale)"), 18,
                   "middle"))
    out.append(txt(58, 355, L(lang, "每项目期望价值（单位：项目每年开发成本）",
                              "Expected value per project (units: one year's development cost)"),
                   18 if zh else 16, "middle", extra=' transform="rotate(-90 58 355)"'))
    for data, colour, dash in ((F3_CONT, P1, ""), (F3_COST, P2, "14 8"), (F3_READ, INK, "3 6")):
        pts = [(X(h), Y(v)) for h, v in zip(F3_X, data)]
        out.append(path(pts, colour, 3.5, dash))
        out += [dot(x, y, 5.5, colour) for x, y in pts]
    lx, ly = 465, 393
    out.append(rect(lx, ly, 520, 132, BG, rx=8))
    out.append(rect(lx, ly, 520, 132, P1, ".04", rx=8, stroke="currentColor", sw=0.6))
    legend = [(P1, "", L(lang, "信息持续到达，无评审成本", "Continuous information, no review cost")),
              (P2, "14 8", L(lang, "信息持续到达，每次评审成本 0.02",
                             "Continuous information, review cost 0.02 each")),
              (INK, "3 6", L(lang, "信息只在第 2、4 年读出时揭示",
                             "Information only at the year-2 and year-4 readouts"))]
    for i, (c, d, lab) in enumerate(legend):
        y = ly + 32 + i * 38
        out += [line(lx + 18, y, lx + 66, y, c, "1", 3.5, d),
                txt(lx + 80, y + 6, lab, 18 if zh else 16)]
    return svg(1080, 700, L(lang, "评审节奏与每项目期望价值（示意模型）",
                            "Review cadence and expected value per project (illustrative model)"),
               out)


# ------------------------------------------------------------ figure 4: timing of hand-off

K = 0.7037222677979313          # fitted so that the losses at years 2 and 4 are 0.16 and 0.10
B = 2.9281326354838133
C = 1.0


def r1(t):
    return C + B * (math.exp(-K * t) - math.exp(-3 * K))


def gain(tau):
    """∫_0^τ (r1 - c) dt: joint value relative to transferring at t = 0."""
    return B * ((1 - math.exp(-K * tau)) / K - tau * math.exp(-3 * K))


def fig4(lang):
    zh = lang == "zh"
    X = lambda t: 140 + t * 148
    out = [txt(140, 54, L(lang, "A　期望价值增长速率：原开发者 vs 潜在接手方",
                          "A   Rate of expected-value growth: original developer vs potential "
                          "acquirer"), 21 if zh else 18, weight="700")]
    # panel A
    YA = lambda r: 380 - r * 78
    out += [line(140, 90, 140, 380, w=2), line(140, 380, 1030, 380, w=2)]
    out += [line(X(t), 380, X(t), 387, w=2) for t in range(7)]
    out.append(txt(90, 215, L(lang, "速率", "Rate"), 18, "middle",
                   extra=' transform="rotate(-90 90 215)"'))
    out.append(path([(X(t / 20), YA(r1(t / 20))) for t in range(0, 121)], P1, 3.5))
    out += [line(140, YA(C), 1030, YA(C), INK, "1", 3, "10 6"),
            txt(185, 133, L(lang, "原开发者（例如早期发现型公司）",
                            "Original developer (e.g. an early-discovery company)"),
                19 if zh else 16, fill=P1),
            txt(1030, 288, L(lang, "潜在接手方（例如大型药企）",
                             "Potential acquirer (e.g. a large pharma company)"),
                19 if zh else 16, "end"),
            line(X(3), YA(C), X(3), 380, P1, ".8", 1.5, "3 4"), dot(X(3), YA(C), 8, P1),
            txt(X(3) + 16, 368, L(lang, "两条曲线相交：最优转让时点",
                                  "Curves cross: the optimal transfer time"),
                19 if zh else 16, weight="700", fill=P1)]
    # panel B
    out.append(txt(140, 452, L(lang, "B　转让时点 τ 对应的总价值 V(τ)",
                               "B   Joint value V(τ) by transfer time τ"), 21 if zh else 18,
                   weight="700"))
    peak = gain(3)
    YB = lambda g: 760 - g / peak * 240
    out += [line(140, 490, 140, 800, w=2), line(140, 800, 1030, 800, w=2)]
    for t in range(7):
        out += [line(X(t), 800, X(t), 807, w=2), txt(X(t), 834, t, 17, "middle")]
    out.append(txt(1052, 836, L(lang, "年", "yrs"), 18))
    out.append(path([(X(t / 20), YB(gain(t / 20))) for t in range(0, 121)], P1, 3.5))
    out += [line(X(2), YB(gain(2)), X(3), YB(gain(2)), op=".4", w=1, dash="3 3"),
            dot(X(3), YB(peak), 9, P1),
            txt(X(3), YB(peak) - 22, L(lang, "连续评估：τ≈3.0 年", "Continuous evaluation: τ ≈ 3.0 yrs"),
                20 if zh else 17, "middle", "700", fill=P1)]
    out += [diamond(X(t), YB(gain(t)), 11) for t in (0, 2, 4, 6)]
    out += [txt(X(2) - 22, YB(gain(2)) + 8, L(lang, "第 2 年转让损失 0.16",
                                              "Transfer at year 2: loses 0.16"),
                18 if zh else 16, "end"),
            txt(X(4) + 22, YB(gain(4)) + 8, L(lang, "第 4 年转让损失 0.10",
                                              "Transfer at year 4: loses 0.10"),
                18 if zh else 16),
            diamond(166, 773, 8),
            txt(182, 780, L(lang, "阶段门只允许在第 0、2、4、6 年决策",
                            "Stage gates allow decisions only at years 0, 2, 4 and 6"),
                18 if zh else 16),
            txt(140, 867, L(lang, "示意模型：网格间距为 h 时，错过极值的期望损失约为 |V″|·h²/24",
                            "Illustrative model: with grid spacing h, the expected loss from "
                            "missing the optimum is about |V″|·h²/24"), 17 if zh else 15,
                op=".55")]
    return svg(1080, 890, L(lang, "换手时机的确定性示意模型", "A deterministic illustrative model of "
                                    "hand-off timing"), out)


# ------------------------------------------------------------ figure 5: AI infrastructure

F5_LAYERS = [
    ("交互层", "Interaction layer",
     ["信念分布、变化原因、距边界远近、最值得获取的信息"],
     ["Belief distributions, why they changed, distance to the boundaries,",
      "and the information most worth getting next"]),
    ("审计与权限层", "Audit & access layer",
     ["版本管理、决策日志、事后校准；访问权限与盲态/合作方数据隔离"],
     ["Versioning, decision log, post-hoc calibration; access rights and",
      "separation of blinded and partner data"]),
    ("决策层", "Decision layer",
     ["各行动的期望价值、信息价值引擎、组合配置与边界触发"],
     ["Expected value of each action, value-of-information engine, portfolio",
      "allocation and boundary triggers"]),
    ("模型层", "Model layer",
     ["分层贝叶斯先验与动态借用、PK/PD 与疾病进展模型、成功率预测"],
     ["Hierarchical Bayesian priors and dynamic borrowing, PK/PD and",
      "disease-progression models, success-rate prediction"]),
    ("数据层", "Data layer",
     ["统一证据图谱：内部实验、临床运营、安全性、真实世界、竞品与文献"],
     ["Unified evidence graph: in-house experiments, clinical operations, safety,",
      "real-world data, competitors and literature"]),
]


def fig5(lang):
    zh = lang == "zh"
    out = []
    bh, gap, y0 = 118, 26, 60
    for i, (z, e, dz, de) in enumerate(F5_LAYERS):
        y = y0 + i * (bh + gap)
        decision = i == 2
        out.append(rect(60, y, 760, bh, BG, rx=12))
        out.append(rect(60, y, 760, bh, P1, ".14" if decision else ".06", rx=12, stroke=P3, sw=2))
        out.append(txt(96, y + 50, z if zh else e, 28 if zh else 24, weight="700",
                       fill=P1 if decision else INK))
        for j, row in enumerate(dz if zh else de):
            out.append(txt(96, y + 86 + j * 22, row, 19 if zh else 16, op=".85"))
        if i < 4:
            out += [line(440, y + bh + gap - 2, 440, y + bh + 6, w=2),
                    head(440, y + bh + 4, -90, size=14)]
    # decision makers
    out += [rect(860, 60, 180, 694, BG, rx=16),
            rect(860, 60, 180, 694, P1, ".04", rx=16, stroke=P1, sw=3),
            txt(950, 140, L(lang, "决策者", "Decision makers"), 24 if zh else 19, "middle", "700",
                fill=P1)]
    roles = L(lang, ["定义价值函数", "设定章程边界", "批准越界行动", "判断模型外因素"],
              [["Define the", "value function"], ["Set the", "charter limits"],
               ["Approve actions", "past the limits"], ["Judge what the", "model leaves out"]])
    for i, r in enumerate(roles):
        y = 250 + i * (56 if zh else 76)
        if zh:
            out.append(txt(950, y, r, 19, "middle"))
        else:
            out += [txt(950, y - 8, r[0], 16, "middle"), txt(950, y + 13, r[1], 16, "middle")]
    out += [line(826, 119, 846, 119, P1, "1", 2.5), head(858, 119, 0, P1, 14),
            line(858, 407, 826, 407, P1, "1", 2.5), head(822, 407, 180, P1, 14)]
    out.append(txt(60, 796, L(lang, "数据自下而上流动；决策者通过章程与价值函数约束决策层，通过交互层获取信息",
                              "Data flows upwards; decision makers constrain the decision layer through "
                              "the charter and value function,"), 18 if zh else 15, op=".55"))
    if not zh:
        out.append(txt(60, 818, "and get information through the interaction layer", 15, op=".55"))
    return svg(1080, 840, L(lang, "信念流决策的 AI 基础设施分层",
                            "The AI infrastructure layers of belief-flow decisions"), out)


if __name__ == "__main__":
    for lang in ("en", "zh"):
        d = os.path.join(ROOT, "_includes", "charts", "belief-flow", lang)
        os.makedirs(d, exist_ok=True)
        for fname, fn in (("fig1.svg", fig1), ("fig2.svg", fig2), ("fig3.svg", fig3),
                          ("fig4.svg", fig4), ("fig5.svg", fig5)):
            p = os.path.join(d, fname)
            open(p, "w", encoding="utf-8").write(fn(lang))
            print("wrote", os.path.relpath(p, ROOT))
