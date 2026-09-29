#!/usr/bin/env python3
"""Generate the MHS architecture diagram as inline SVG, in both languages.

    python3 script/make_mhs_diagram.py

The WeChat original is a raster with the Chinese labels burnt in. Redrawn here
for the same reasons as script/make_charts.py: the English post needs its own
labels, and inlined via {% include %} the text and outlines are currentColor
and follow the site's light/dark toggle. Only the highlighted core layer
carries a fixed colour.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLUE = "#2274bd"
FONT = ('font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\','
        "'Helvetica Neue',Arial,'PingFang SC','Hiragino Sans GB',"
        "'Microsoft YaHei','Noto Sans CJK SC',sans-serif\"")

T = {
    "zh": {
        "title": "MHS 分层架构：安全限值在设备层强制执行",
        "agent": "智能体（Claude 或任意模型的 agent harness）",
        "agent_sub": "推理、规划、读取数据、实时改参数；遇到风险操作可暂停等待人工确认",
        "access": [("MCP", "逐步调用，交互式探索"),
                   ("命令行 CLI", "脚本化操作与调试"),
                   ("代码文件（API）", "串联多设备指令，跑长任务")],
        "core": "MHS 标准驱动（核心层）",
        "core_lines": ["一小组原语，如 read（读取温度）、write（设定温度）",
                       "标准化发现 + MHS 状态字典：多程序共享读写设备数据",
                       "自然语言标签 → 参考文件：能测什么、能调什么、安全限值是多少",
                       "设备级安全限值：超出厂商规格的指令在执行前被拦截"],
        "vendor": "厂商原生接口",
        "vendor_sub": "SDK / API 等；无 API 的仪器可暂以模拟 GUI 操作接入（CMU 案例）",
        "devices": "物理设备",
        "device_list": ["移液工作站", "读板仪", "机械臂", "显微镜", "激光与光学", "qPCR / 相机"],
        "foot": "长任务由代码串联、设备以原生速度执行；智能体只在需要推理的节点介入",
    },
    "en": {
        "title": "MHS layers: safety limits are enforced at the device layer",
        "agent": "Agent (Claude, or any model's agent harness)",
        "agent_sub": "Reasons, plans, reads data, adjusts parameters live; "
                     "can pause for human confirmation before a risky action",
        "access": [("MCP", "Step-by-step calls, interactive exploration"),
                   ("Command line (CLI)", "Scripted operation and debugging"),
                   ("Code files (API)", "Chain multi-device commands for long runs")],
        "core": "MHS standard driver (core layer)",
        "core_lines": ["A small set of primitives, e.g. read (read temperature), "
                       "write (set temperature)",
                       "Standardised discovery + MHS state dictionary: "
                       "device data shared by many programs",
                       "Natural-language tags → reference file: what it measures, "
                       "what it adjusts, its safety limits",
                       "Device-level safety limits: commands beyond the vendor's spec "
                       "are blocked before execution"],
        "vendor": "Vendor native interfaces",
        "vendor_sub": "SDKs, APIs, etc.; an instrument with no API can be driven "
                      "through its GUI for now (the CMU case)",
        "devices": "Physical devices",
        "device_list": ["Liquid handler", "Plate reader", "Robot arm", "Microscope",
                        "Lasers & optics", "qPCR / camera"],
        "foot": "Long runs are chained in code and devices run at native speed; "
                "the agent steps in only where reasoning is needed",
    },
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=15, anchor="middle", weight="400", op="1"):
    return ('  <text x="%d" y="%d" font-size="%d" text-anchor="%s" font-weight="%s" '
            'fill="currentColor" fill-opacity="%s">%s</text>' % (x, y, size, anchor, weight,
                                                                 op, esc(s)))


def box(x, y, w, h, stroke="currentColor", sop=".25", fill="none", fop="0", sw=1.5):
    return ('  <rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" '
            'fill-opacity="%s" stroke="%s" stroke-opacity="%s" stroke-width="%s"/>'
            % (x, y, w, h, fill, fop, stroke, sop, sw))


def arrow(x, y1, y2):
    return ('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="currentColor" '
            'stroke-opacity=".35" stroke-width="1.5"/>\n'
            '  <path d="M%d %d l-5 -8 h10 z" fill="currentColor" fill-opacity=".35"/>'
            % (x, y1, x, y2 - 6, x, y2))


def diagram(lang):
    t = T[lang]
    L, W = 36, 1008                       # outer boxes span x = 36 … 1044
    out = [txt(L, 44, t["title"], 19, "start", "600")]

    # agent
    out += [box(L, 76, W, 80), txt(540, 108, t["agent"], 17, weight="600"),
            txt(540, 136, t["agent_sub"], 14, op=".7")]

    # three access routes
    cw, gap = 320, 24
    for i, (head, sub) in enumerate(t["access"]):
        x = L + i * (cw + gap)
        cx = x + cw // 2
        out += [arrow(cx, 156, 182), box(x, 182, cw, 90),
                txt(cx, 218, head, 17, weight="600"), txt(cx, 248, sub, 14, op=".7")]

    # core driver layer
    for i in range(3):
        out.append(arrow(L + i * (cw + gap) + cw // 2, 272, 306))
    out += [box(L, 306, W, 170, BLUE, "1", BLUE, ".08", 2.5),
            txt(58, 342, t["core"], 17, "start", "600")]
    for i, s in enumerate(t["core_lines"]):
        out.append(txt(58, 376 + i * 26, s, 15, "start"))

    # vendor interfaces
    out += [arrow(540, 476, 510), box(L, 510, W, 80),
            txt(540, 543, t["vendor"], 17, weight="600"),
            txt(540, 572, t["vendor_sub"], 14, op=".7")]

    # devices
    out += [arrow(540, 590, 624), box(L, 624, W, 128),
            txt(58, 656, t["devices"], 17, "start", "600")]
    dw, dg = 142, (W - 44 - 6 * 142) // 5
    for i, name in enumerate(t["device_list"]):
        x = L + 22 + i * (dw + dg)
        out += [box(x, 674, dw, 58, sop=".3"), txt(x + dw // 2, 709, name, 15)]

    out.append(txt(L, 790, t["foot"], 14, "start", op=".6"))
    return ('<svg class="chart" viewBox="0 0 1080 810" role="img" aria-label="%s" %s>\n'
            '  <title>%s</title>\n%s\n</svg>\n'
            % (esc(t["title"]), FONT, esc(t["title"]), "\n".join(out)))


if __name__ == "__main__":
    for lang in T:
        d = os.path.join(ROOT, "_includes", "charts", "mhs", lang)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "architecture.svg")
        open(path, "w", encoding="utf-8").write(diagram(lang))
        print("wrote", os.path.relpath(path, ROOT))
