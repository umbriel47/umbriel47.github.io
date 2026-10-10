#!/usr/bin/env python3
"""Generate the four charts for the OpenAI-math meta-analysis post as SVG.

    python3 script/make_openai_math_charts.py

The WeChat originals are rasters with Chinese labels burnt in; these are rebuilt
from the data, in both languages, for the same reasons as script/make_charts.py.
Text, axes and the darkest series are currentColor, so they follow the site's
light/dark toggle; purple text carries .accent-text so style.css can lighten it
on the dark theme.

Figure 1's unlabelled one-unit segments were reconstructed from the row totals;
the reconstruction reproduces every total in the text (217 / 74 / 53 / 18 / 10
by conclusion type, and each discipline's count).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P1, ORANGE, P3, P4 = "#5b4fc4", "#d95f2b", "#b3abf0", "#d6d1f7"
INK = "currentColor"
GREY = "#8a86a3"
DARK_TEXT = "#1b1640"
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=18, anchor="start", weight="400", fill=INK, op="1"):
    cls = ' class="accent-text"' if fill == P1 else ""
    paint = (' style="fill: %s"' % fill if fill.startswith("var(")
             else ' fill="%s" fill-opacity="%s"' % (fill, op))
    return ('  <text%s x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" font-weight="%s"%s>'
            '%s</text>' % (cls, x, y, size, anchor, weight, paint, esc(s)))


def rect(x, y, w, h, fill, op="1"):
    return ('  <rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity="%s"/>'
            % (x, y, max(w, 0), h, fill, op))


def line(x1, y1, x2, y2, op=".15", w=1, stroke=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, stroke, op, w, d))


def svg(w, h, desc, body):
    return ('<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n'
            % (w, h, esc(desc), FONT, esc(desc), "\n".join(body)))


def label_on(colour):
    """Text colour for a number printed inside a bar of this colour."""
    if colour == INK:
        return "var(--bg, #fff)"
    return "#fff" if colour in (P1, ORANGE) else DARK_TEXT


# ------------------------------------------------------------ shared names

DISCIPLINES = {
    "tcs": ("理论计算机科学", "Theoretical computer science"),
    "comb": ("组合数学", "Combinatorics"),
    "agcg": ("代数与复几何", "Algebraic & complex geometry"),
    "nt": ("数论", "Number theory"),
    "prob": ("概率论与统计力学", "Probability & stat. mechanics"),
    "dg": ("微分几何", "Differential geometry"),
    "mp": ("数学物理", "Mathematical physics"),
    "oa": ("算子代数", "Operator algebras"),
    "alg": ("代数", "Algebra"),
    "top": ("拓扑学", "Topology"),
    "rca": ("实分析与复分析", "Real & complex analysis"),
    "pde": ("偏微分方程", "PDEs"),
    "cmg": ("凸几何与度量几何", "Convex & metric geometry"),
    "gt": ("群论", "Group theory"),
    "ds": ("动力系统与遍历论", "Dynamics & ergodic theory"),
    "fa": ("泛函分析", "Functional analysis"),
    "logic": ("数理逻辑", "Mathematical logic"),
}


def name(key, lang):
    return DISCIPLINES[key][0 if lang == "zh" else 1]


# ------------------------------------------------------------ figure 1

# (solved, negative/counterexample, partial, improved bound, other)
F1_DATA = [("tcs", (19, 5, 2, 12, 2)), ("comb", (22, 10, 1, 4, 0)),
           ("agcg", (17, 8, 10, 0, 1)), ("nt", (20, 1, 10, 0, 0)),
           ("prob", (22, 0, 6, 0, 1)), ("dg", (17, 8, 3, 0, 1)),
           ("mp", (18, 3, 3, 0, 1)), ("oa", (12, 6, 0, 0, 1)),
           ("alg", (6, 8, 4, 0, 0)), ("top", (10, 6, 2, 0, 0)),
           ("rca", (7, 1, 8, 0, 0)), ("pde", (10, 4, 1, 0, 1)),
           ("cmg", (9, 3, 1, 2, 0)), ("gt", (9, 5, 0, 0, 0)),
           ("ds", (9, 2, 1, 0, 0)), ("fa", (5, 3, 1, 0, 2)), ("logic", (5, 1, 0, 0, 0))]
F1_COLOURS = (P1, ORANGE, P3, INK, P4)
F1 = {
    "zh": {"title": "372 个结果族的学科分布与结论类型",
           "sub": "按 OpenAI 目录的 17 个学科分类；结论类型由一目半逐族判读，口径见正文",
           "legend": ["声称完整解决", "否定或给出反例", "部分进展", "改进界", "其他新结果"],
           "axis": "结果族数量"},
    "en": {"title": "372 result families by discipline and type of conclusion",
           "sub": "Disciplines as in OpenAI's 17-way catalogue; conclusion types judged family "
                  "by family by 一目半 (see text)",
           "legend": ["Claimed full solution", "Negative / counterexample", "Partial progress",
                      "Improved bound", "Other new result"],
           "axis": "Number of result families"},
}


def fig1(lang):
    t = F1[lang]
    ax, unit = (300, 17.5) if lang == "zh" else (330, 16.75)
    out = [txt(40, 58, t["title"], 28, weight="700"), txt(40, 92, t["sub"], 17, op=".65")]
    lx = 40
    widths = (175, 195, 140, 110, 130) if lang == "zh" else (210, 245, 175, 160, 0)
    lys = (132, 132, 132, 132, 132) if lang == "zh" else (132, 132, 132, 132, 162)
    for i, (lab, c) in enumerate(zip(t["legend"], F1_COLOURS)):
        if lang == "en" and i == 4:
            lx = 40
        out += [rect(lx, lys[i] - 15, 18, 18, c, ".92" if c == INK else "1"),
                txt(lx + 26, lys[i], lab, 17)]
        lx += widths[i]
    top = 185 if lang == "zh" else 210
    for v in range(0, 41, 10):
        x = ax + v * unit
        out.append(line(x, top - 10, x, top + 17 * 40 + 5))
        out.append(txt(x, top + 17 * 40 + 30, v, 15, "middle", op=".6"))
    out.append(txt(ax + 20 * unit, top + 17 * 40 + 62, t["axis"], 16, "middle", op=".6"))
    for i, (key, vals) in enumerate(F1_DATA):
        y = top + i * 40
        out.append(txt(ax - 14, y + 20, name(key, lang), 18, "end"))
        x = ax
        for v, c in zip(vals, F1_COLOURS):
            if not v:
                continue
            w = v * unit
            out.append(rect(x, y, w - 1, 28, c, ".92" if c == INK else "1"))
            if v >= 2:
                out.append(txt(x + w / 2, y + 19.5, v, 14, "middle", fill=label_on(c)))
            x += w
        out.append(txt(x + 8, y + 20.5, sum(vals), 17, weight="700"))
    return svg(1080, top + 17 * 40 + 80, t["title"], out)


# ------------------------------------------------------------ figure 2

F2_DECADES = [(1870, 1), (1880, 0), (1890, 0), (1900, 5), (1910, 1), (1920, 2), (1930, 7),
              (1940, 8), (1950, 17), (1960, 21), (1970, 52), (1980, 46), (1990, 39),
              (2000, 42), (2010, 34), (2020, 8)]
F2 = {
    "zh": {"title": "这些问题是什么时候被提出的",
           "sub": ["可定年的 283 个结果族，按问题首次提出的年代计数；另有 89 个无法可靠定年，未计入"],
           "median": "中位数 1986",
           "stats": "四分位：1971 / 1986 / 2004　·　1950 年以前提出：24 个　·　2010 年以后提出：42 个",
           "note": "年代为首次提出年份，多数依据文献记载与综述；单个年份可能有数年误差，抽样核查结果见正文"},
    "en": {"title": "When were these problems first posed?",
           "sub": ["The 283 datable result families, counted by the decade the problem was "
                   "first posed;", "89 more could not be dated reliably and are excluded"],
           "median": "median 1986",
           "stats": "Quartiles: 1971 / 1986 / 2004  ·  posed before 1950: 24  ·  posed from "
                    "2010 on: 42",
           "note": "Decade of first posing, mostly from the literature and surveys; individual "
                   "years may be off by a few years (sampled check in the text)"},
}


def fig2(lang):
    t = F2[lang]
    x0, bw, gap = 110, 46, 11.4
    base, unit = 600, 7.35
    out = [txt(60, 58, t["title"], 28, weight="700")]
    out += [txt(60, 98 + i * 24, row, 17, op=".65") for i, row in enumerate(t["sub"])]
    for v in range(0, 51, 10):
        y = base - v * unit
        out += [line(x0 - 20, y, 1030, y, ".12"), txt(x0 - 30, y + 5, v, 15, "end", op=".6")]
    for i, (dec, n) in enumerate(F2_DECADES):
        x = x0 + i * (bw + gap)
        c = P3 if dec < 1950 else P1
        if n:
            out += [rect(x, base - n * unit, bw, n * unit, c),
                    txt(x + bw / 2, base - n * unit - 8, n, 16, "middle", "700")]
        out.append(txt(x + bw / 2, base + 27, dec, 14, "middle", op=".6"))
    mx = x0 + 11 * (bw + gap) + bw / 2           # the 1980s bar
    out += ['  <path d="M%.1f 632 l-9 12 h18 z" fill="%s"/>' % (mx, ORANGE),
            '  <text x="%.1f" y="664" font-size="15" text-anchor="middle" fill="%s">%s</text>'
            % (mx, ORANGE, esc(t["median"])),
            txt(60, 697, t["stats"], 17),
            txt(60, 726, t["note"], 14, op=".6")]
    return svg(1080, 746, t["title"], out)


# ------------------------------------------------------------ figure 3

F3_DATA = [("logic", 6, 6), ("fa", 10, 11), ("comb", 33, 37), ("cmg", 13, 15), ("gt", 12, 14),
           ("tcs", 32, 40), ("ds", 9, 12), ("oa", 14, 19), ("pde", 11, 16), ("mp", 17, 25),
           ("prob", 19, 29), ("rca", 9, 16), ("dg", 15, 29), ("nt", 16, 31), ("alg", 9, 18),
           ("agcg", 7, 36), ("top", 3, 18)]
F3 = {
    "zh": {"title": "哪些学科附带了 Lean 形式化",
           "sub": "每个学科中附有 Lean 范围说明的结果族占比；全体为 235/372（63%）",
           "note": "注意：附有说明不等于主定理已被完整形式化，仓库清单把整体状态标为「部分进展」、审查状态为「未核查」",
           "avg": "全体平均"},
    "en": {"title": "Which disciplines come with Lean formalisation",
           "sub": "Share of result families in each discipline with a Lean scope note; "
                  "overall 235/372 (63%)",
           "note": "Note: a scope note does not mean the main theorem is fully formalised; the "
                   "repository marks its overall status as “partial progress”, review "
                   "“unchecked”",
           "avg": "overall average"},
}


def fig3(lang):
    t = F3[lang]
    ax, width = (300, 660) if lang == "zh" else (330, 630)
    top = 178
    out = [txt(60, 58, t["title"], 28, weight="700"), txt(60, 104, t["sub"], 17, op=".65"),
           txt(60, 134, t["note"], 14 if lang == "zh" else 13, op=".6")]
    for p in (0, 25, 50, 75, 100):
        x = ax + width * p / 100
        out += [line(x, top - 14, x, top + 17 * 38 + 4),
                txt(x, top + 17 * 38 + 30, "%d%%" % p, 15, "middle", op=".6")]
    avg_x = ax + width * 235 / 372
    out += ['  <line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2" '
            'stroke-dasharray="6 6"/>' % (avg_x, top - 14, avg_x, top + 17 * 38 + 4, ORANGE),
            '  <text x="%.1f" y="%d" font-size="16" text-anchor="middle" fill="%s">%s</text>'
            % (avg_x, top + 17 * 38 + 62, ORANGE, esc(t["avg"]))]
    for i, (key, k, n) in enumerate(F3_DATA):
        y = top + i * 38
        out += [txt(ax - 14, y + 18, name(key, lang), 17, "end"),
                rect(ax, y, width, 24, P1, ".14"),
                rect(ax, y, width * k / n, 24, P1),
                txt(ax + width + 12, y + 18, "%d/%d" % (k, n), 16)]
    return svg(1080, top + 17 * 38 + 84, t["title"], out)


# ------------------------------------------------------------ figure 4

CAT = {"auto": P1, "aided": P3, "formal": INK, "ml": ORANGE, "eval": GREY}
F4_EVENTS = [
    ("1956", "auto", "逻辑理论家：证明《数学原理》第二章前 52 条定理中的 38 条",
     "Logic Theorist proves 38 of the first 52 theorems in chapter 2 of Principia"),
    ("1958–60", "auto", "王浩在 IBM 704 上机械证明《数学原理》中的数百条命题",
     "Hao Wang proves hundreds of Principia's propositions mechanically on an IBM 704"),
    ("1965", "auto", "Robinson 提出归结原理，奠定一阶自动定理证明的基础",
     "Robinson's resolution principle founds first-order automated theorem proving"),
    ("1967", "formal", "de Bruijn 启动 Automath，最早的证明检验语言之一",
     "de Bruijn starts Automath, one of the first proof-checking languages"),
    ("1976", "aided", "四色定理：Appel 与 Haken 的计算机辅助证明",
     "Four colour theorem: Appel and Haken's computer-assisted proof"),
    ("1996", "auto", "EQP 程序证明 Robbins 猜想，自动证明器解决的著名开放问题",
     "EQP proves the Robbins conjecture, a famous open problem solved by a prover"),
    ("2005", "formal", "Gonthier 等用 Coq 完成四色定理的形式化证明",
     "Gonthier et al. formalise the four colour theorem in Coq"),
    ("2013", "formal", "Lean 定理证明器诞生；2017 年起社区建设 mathlib",
     "The Lean prover is born; the community builds mathlib from 2017"),
    ("2014", "formal", "Flyspeck 完成开普勒猜想的形式化证明",
     "Flyspeck completes the formal proof of the Kepler conjecture"),
    None,
    ("2020.09", "ml", "OpenAI GPT-f：语言模型为 Metamath 生成被收录的证明",
     "OpenAI GPT-f: a language model writes proofs accepted into Metamath"),
    ("2021.12", "ml", "DeepMind 与数学家合作，机器学习引导纽结论与表示论新发现",
     "DeepMind and mathematicians: ML guides new results in knot and representation theory"),
    ("2022.07", "formal", "Liquid Tensor 实验完成，Scholze 的定理被 Lean 完整核验",
     "Liquid Tensor Experiment done: Scholze's theorem fully checked in Lean"),
    ("2023.12", "ml", "FunSearch：LLM 引导的程序搜索改进帽集下界",
     "FunSearch: LLM-guided program search improves cap-set lower bounds"),
    ("2024.07", "ml", "AlphaProof + AlphaGeometry 2 达到 IMO 银牌水平",
     "AlphaProof + AlphaGeometry 2 reach IMO silver-medal level"),
    ("2025.07", "ml", "OpenAI 与 Gemini Deep Think 在 IMO 2025 达到金牌分数线",
     "OpenAI and Gemini Deep Think reach the gold-medal score at IMO 2025"),
    ("2025.10", "eval", "GPT-5「解决埃尔德什问题」风波：答案实为已有文献",
     "The GPT-5 “Erdős problems” episode: the answers were existing literature"),
    ("2026.02", "eval", "First Proof：11 位数学家用 10 道未发表问题测试 AI",
     "First Proof: 11 mathematicians test AI on 10 unpublished problems"),
    ("2026.05", "ml", "OpenAI 模型否定埃尔德什 1946 年单位距离猜想，获外部数学家核查",
     "OpenAI model disproves Erdős's 1946 unit-distance conjecture; checked externally"),
    ("2026.07", "ml", "Anthropic 研究者发布雅可比猜想三维反例，归功于 Claude 模型",
     "Anthropic researcher posts a 3-D Jacobian-conjecture counterexample, credited to Claude"),
    ("2026.08", "ml", "OpenAI「Astra」十项结果附 Lean 证书；Anthropic 将 ζ 零点临界线占比下界提至 67.2%",
     "OpenAI's ten “Astra” results with Lean certificates; Anthropic lifts the ζ "
     "critical-line share to 67.2%"),
    ("2026.09", "eval", "OpenAI 宣称 Navier–Stokes 爆破方向结果；Fields 奖得主联名批评仓促发布",
     "OpenAI claims a Navier–Stokes blow-up result; Fields medallists criticise rushed releases"),
    ("2026.10", "ml", "OpenAI 公开 722 篇手稿、372 个结果族",
     "OpenAI releases 722 manuscripts in 372 result families"),
]
F4 = {
    "zh": {"title": "机器与数学证明：七十年时间线",
           "sub": "年份为事件公布或完成时间；2026 年的多数结果尚未经过同行评审",
           "phases": ["第一阶段 · 符号推理与计算机辅助证明（1956–2019）",
                      "第二阶段 · 神经网络与大语言模型（2020–2026）"],
           "legend": [("auto", "自动推理"), ("aided", "计算机辅助证明"),
                      ("formal", "形式化与证明助手"), ("ml", "机器学习 / 大模型"),
                      ("eval", "评测与争议")],
           "size": 19},
    "en": {"title": "Machines and mathematical proof: a seventy-year timeline",
           "sub": "Dates are when events were announced or completed; most 2026 results have "
                  "not been peer reviewed",
           "phases": ["Phase 1 · Symbolic reasoning and computer-assisted proof (1956–2019)",
                      "Phase 2 · Neural networks and large language models (2020–2026)"],
           "legend": [("auto", "Automated reasoning"), ("aided", "Computer-assisted proof"),
                      ("formal", "Formalisation & proof assistants"), ("ml", "ML / LLMs"),
                      ("eval", "Benchmarks & controversy")],
           "size": 16},
}


def phase_band(y):
    """Tinted phase header, backed by the page colour so the spine doesn't show through."""
    return ('  <rect x="60" y="%d" width="960" height="44" rx="6" style="fill: var(--bg, #fff)"/>\n'
            '  <rect x="60" y="%d" width="960" height="44" rx="6" fill="%s" fill-opacity=".12"/>'
            % (y, y, P1))


def fig4(lang):
    t = F4[lang]
    out = [txt(60, 62, t["title"], 28, weight="700"), txt(60, 104, t["sub"], 17, op=".65")]
    spine_x, y = 230, 172
    out.append(line(spine_x, 160, spine_x, 0, "1", 3, P3))   # placeholder, fixed below
    spine_idx = len(out) - 1
    phase = 0
    out += [phase_band(y), txt(80, y + 29, t["phases"][phase], 20 if lang == "zh" else 18,
                                  weight="700")]
    y += 72
    for ev in F4_EVENTS:
        if ev is None:
            y += 4
            phase += 1
            out += [phase_band(y),
                    txt(80, y + 29, t["phases"][phase], 20 if lang == "zh" else 18,
                        weight="700")]
            y += 72
            continue
        date, cat, zh, en = ev
        c = CAT[cat]
        out += [txt(200, y + 7, date, 19, "end", "700"),
                '  <circle cx="%d" cy="%d" r="9" fill="%s"/>' % (spine_x, y, c),
                txt(256, y + 7, zh if lang == "zh" else en, t["size"])]
        y += 46
    out[spine_idx] = line(spine_x, 160, spine_x, y - 20, ".55", 3, P1)
    y += 30
    if lang == "zh":
        slots = [(60 + i * 200, y) for i in range(5)]
    else:
        slots = [(60, y), (300, y), (580, y), (60, y + 32), (300, y + 32)]
    for (cat, lab), (lx, ly) in zip(t["legend"], slots):
        out += ['  <circle cx="%d" cy="%d" r="9" fill="%s"/>' % (lx + 9, ly, CAT[cat]),
                txt(lx + 26, ly + 6, lab, 17 if lang == "zh" else 16)]
    return svg(1080, slots[-1][1] + 40, t["title"], out)


if __name__ == "__main__":
    for lang in ("en", "zh"):
        d = os.path.join(ROOT, "_includes", "charts", "openai-math", lang)
        os.makedirs(d, exist_ok=True)
        for fname, fn in (("fig1.svg", fig1), ("fig2.svg", fig2), ("fig3.svg", fig3),
                          ("fig4.svg", fig4)):
            path = os.path.join(d, fname)
            open(path, "w", encoding="utf-8").write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))
