---
layout: post
title: "从调用工具到操作仪器：Anthropic 模型硬件标准（MHS）综述"
date: 2026-09-29 08:55:00 +0800
lang: zh
ref: model-hardware-standard
tags: [science]
wide: true
wechat_url: "https://mp.weixin.qq.com/s/N3kSguRUtGkuKZQjSImaBQ"
description: "MHS（模型硬件标准）是 Anthropic 于 2026 年 8 月 27 日以研究预览形式发布的一套共享规范，旨在让 AI 智能体能够发现、理解并安全操作实验室与制造设备，外界常称之为“硬件版 MCP”。"
---

<figure class="lead">
  <img src="/assets/img/posts/model-hardware-standard/hero.png" alt="一束光纤分出几路，连向实验台上的移液工作站、机械臂和显微镜">
</figure>

## 摘要

MHS（Model Hardware Standard，模型硬件标准）是 Anthropic 于 2026 年 8 月 27 日以研究预览（research preview）形式发布的一套共享规范，旨在让 AI 智能体能够发现、理解并安全操作实验室与制造设备。Fortune 将其称为 Anthropic 首次涉足物理 AI；由于它以 MCP 为主要接入协议，外界常称之为“硬件版 MCP”。

本文的核心判断有三点：

- **定位**：MHS 要解决的是“集成碎片化”问题，而非“自主性”本身——把设备接入从数周压缩到数小时，并在设备层强制执行安全限值。
- **证据**：6 个公开案例给出了扎实的概念验证数据（如 QuEra 激光重锁成功率从 58% 提升至 99.3%；CMU 从设备就绪到完成量效曲线仅用约 8 小时，而厂商交付方案通常需数周），但案例全部基于 Claude，跨模型互操作仍停留在设计承诺层面。
- **成熟度**：规范本身尚未公开，外部分析指出其缺少版本化规格、一致性测试、安全威胁模型与治理规则；它目前是一个证据扎实的研究预览，尚未成为事实标准。

## MHS 是什么：为设备写一份“智能体说明书”

MHS 的官方定义是“一种供 AI 智能体安全操作物理设备的共享规范”，首批面向科研实验室与先进制造商。公开案例涉及显微镜、移液工作站、机械臂、读板仪、qPCR 仪、离心机、相机、激光器等设备。

**要解决的问题**：实验室或工厂集成一套硬件通常需要数周到数月；设备接口互不兼容，只能依赖专家编写定制集成代码；大量操作知识（安全范围、物理特性）只存在于手册和工程师的经验中。Anthropic 技术人员 Alek Kemeny 表示：“目前没有一种把模型连到物理设备的通用方式。”（据 R&D World）

**与 MCP 的关系**：MCP（Model Context Protocol，模型上下文协议）负责承载工具调用，MHS 负责描述工具背后的设备——它能测什么、能调什么、有哪些安全限值。按设计，MHS 与模型无关：任何智能体框架都可以通过 MCP、命令行（CLI）或代码 API 访问它。Kemeny 曾把 MCP 比作“AI 连接软件的 USB”（据 Fortune），MHS 可以理解为把这个接口延伸到了硬件。

| 维度 | MCP | MHS |
|---|---|---|
| 发布时间 | 2024 年 11 月 | 2026 年 8 月（研究预览） |
| 连接对象 | 软件工具、数据源 | 物理设备 |
| 核心抽象 | tools / resources / prompts | 标准驱动 + 一小组原语（如 read/write）+ 设备参考文件 |
| 安全边界 | 主要靠客户端授权 | 在设备层强制执行安全限值 |
| 开放状态 | 已开源；2025 年 12 月捐赠给 Linux 基金会旗下的 AAIF（Agentic AI Foundation） | 规范未公开；各设备驱动将公开 |

## 技术路线：五个关键设计

MHS 的技术路线概括为：以极简的标准驱动层屏蔽设备异构性，将操作知识与安全限值编译进驱动，再由智能体通过现有协议调用。

<figure>
  {%- include charts/mhs/zh/architecture.svg -%}
</figure>

自上而下看，智能体只面对统一的驱动接口；设备异构性被封装在驱动层之下，安全边界也在这一层强制执行。

### 1. 一小组原语 + 标准化发现

驱动暴露一小组原语，以 read（读取状态，如“读取温度”）和 write（写入设定，如“设定温度”）为代表；设备以标准格式可被发现，智能体与设备之间不再需要点对点的“翻译程序”。多台仪器的数据汇入 MHS 状态字典——一块可供多个程序同时读写的共享内存区。

### 2. 把隐性知识编译成参考文件

用户以自然语言编写驱动标签（也可以让智能体“采访”设备操作员），驱动据此自动生成参考文件，说明设备能测什么、能调什么、执行哪些安全限值。官方称，这让智能体能够上手“从未见过的设备”。

### 3. 探索与固化分离

开发阶段，智能体在线推理、反复试错；流程成熟后，再固化为确定性、可审查的代码，由代码串联一台或多台设备的驱动指令，跑超出模型在线推理速度的长任务。QuEra 是典型案例：Claude 把线性的激光重锁流程改写为基于仪器读数的决策树脚本，最终脚本运行时无需 AI 参与。Kingy AI将这一模式概括为“一个能调试、测试、监控并留下可审查程序的自动化工程师”，而非“让聊天机器人直接接管工厂”。

### 4. 安全限值在设备层强制执行

MHS 在设备层强制执行安全限值（如激光功率上限），智能体无法越过厂商规格；MarkTechPost将其概括为“限值在驱动里，不在提示词里”。在 CMU 的测试中，人为构造的 6 种故障（如缺板、板旋转）均在设备动作前被拦截。第三方实现也在补强这一层：Fastly 的边缘侧研究原型在转发前校验限值，并加入单设备调用配额（防止硬件磨损）和带哈希身份的审计日志。

### 5. 实验方案与硬件解耦

Tetsuwan 用 MHS 替换了原有的调度器：实验方案中写明所需离心力，系统查询可用的离心机驱动，再由 Claude 根据转子半径换算为转速。这意味着实验方案可以在不同品牌的设备之间迁移。

## 发展历程：从 MCP 到 MHS

从时间线看，MHS 并非孤立产品，而是 Anthropic 近两年“连接软件 → 进入科研工作流 → 执行物理实验”这一路径上的第三步：MCP 提供了协议底座，Claude for Life Sciences 与 Claude Science 积累了科研场景和客户，收购 Coefficient Bio 带来了药物发现团队。前两款科研产品都停留在文献、分析与代码层面，MHS 补上了“动手做实验”这一环。

| 日期 | 事件 | 意义 |
|---|---|---|
| 2024-11 | 发布 MCP | 智能体连接外部工具的开放协议，后成为 MHS 的主要接入协议 |
| 2025-10-20 | 发布 Claude for Life Sciences | Benchling、PubMed、10x Genomics 等连接器，聚焦计算与文献 |
| 2025-12-09 | MCP 捐赠给 Agentic AI Foundation | 协议走向中立治理，为 MHS 的“模型无关”叙事奠定基础 |
| 2026-04-03 | 收购 Coefficient Bio（据报道约 4 亿美元，以股票支付；团队约 10 人） | 创始人来自 Genentech Prescient Design，补齐药物发现能力 |
| 2026-06-30 | Claude Science 公测 | 科研工作台：多智能体 + 60 多项技能 + 算力调度，但不含硬件控制 |
| 2026-08-27 | MHS 研究预览发布；同日发布科学家支持计划 | 首次正式进入物理 AI 领域；与 HHMI Janelia 联合开发 |

**起源**：MHS 源于 Anthropic Beneficial Deployments 团队的 Alek Kemeny 与 HHMI Janelia Spruston 实验室博士后 Arco Bast 的合作：Bast 为让多台仪器互通而编写的共享内存字典，演变为今天的 MHS 状态字典。立项时间与团队规模未公开。

## 现状：研究预览与首批概念验证

截至 2026 年 9 月 28 日，MHS 仍处于研究预览：仅限受邀合作方参与、开放候补名单（modelhardwarestandard.com）、规范未公开。公开证据来自 6 个合作方案例，量化程度较高，但仍属概念验证。

### 首批合作方结果

下表数据均来自 Anthropic 官方公告及合作方博客，尚无独立复现。

| 合作方 | 任务 | 关键结果 | 集成或完成耗时 |
|---|---|---|---|
| QuEra | 量子计算机激光重锁与 PID 调参 | 重锁成功率 58% → 99.3%（基线脚本由 4 人团队耗时数月手写；最终脚本在无 AI 参与的随机扰动测试中成功 695/700 次）；单次恢复从约 150 s 降至多数故障数秒、最难情况约 10–14 s；16 小时无人值守完成 363 次调参实验，伺服环 RMS 误差 15.7 → 1.55 mV | — |
| Carnegie Mellon | 梯度稀释量效曲线 | 整体提速约 3 倍；自动剔除 R² < 0.9 的饱和批次并重新运行至 R² > 0.98；6 种人为故障均被拦截；无 API 的读板仪以模拟人工操作 GUI 的方式接入 | 从设备就绪到完成量效曲线（含一次自主重跑）约 8 小时；厂商方案通常需数周 |
| Tetsuwan Scientific | qPCR 移液编译器闭环优化 | 9,143 次分液、300 种转移类型；多次分液精度的预测比厂商规格准确约 12%（Tetsuwan 博客：45 个留出批次中胜 33 个，p ≈ 0.003；Anthropic 公告作 31/45、p ≈ 0.001，两处不一致）；通过视觉检测到气泡后自动离心恢复 | — |
| Genentech | BCA 蛋白定量的移液参数优化 | 水的最优流速约 140 µL/s（RMSE 0.016），黏稠 BSA 约 10 µL/s（RMSE 0.181）；气泡问题需人工引导 | — |
| University of Washington（Baker/Pinglay 实验室） | qPCR 实时监控、机械臂与移液仪交接 | 实时识别扩增曲线，在关键节点询问研究者是否终止，收到指令后停止反应并转入 4 °C 保存；多轮测试零碰撞 | 6 台仪器用时不到 1 周（含编写驱动） |
| HHMI Janelia | 显微成像光路对准与在线分析 | 原需半天的手动对准与调试压缩为一步 | 新增一台相机的接入时间从数天缩短至几分钟 |

### 预览发布后的进展

- **2026-09-02**：Fastly 发布 edge-mhs 研究原型，在其边缘 MCP 实现上加入限值校验、单设备调用配额与审计日志。
- **2026-09-18**：据 Startup Fortune（引 Reuters）报道，Anthropic 在湾区建成机器人湿实验室，让 Claude 指导真实生物实验、开展被忽视疾病的药物发现；目前仍有人员出于安全进行监督。

### 生态与配套举措

- **厂商**（参与程度不一）：Tecan（Fluent）、Automata（LINQ）、MBF Bioscience（ScanImage）正在加入支持；Universal Robots 计划支持；QIAGEN（QIAsymphony Connect）完成概念验证；Doosan Robotics 在测试；Danaher 仍在探索。
- **开发者生态**：Hugging Face 正在 LeRobot 中加入支持；AWS 向预览参与者提供 Strands Robots 私有预发布版；Raspberry Pi 在相机驱动测试成功后推进多款产品集成。
- **开放策略**：规范在预览期由 Anthropic 主导，计划与合作方完成安全评测后开源并附安全部署指南；各仪器驱动将公开供复用。
- **配套举措**：同日发布的科学家支持计划提供 1 万个 Team 席位，面向学术/非营利机构 PI：标准席位免费一年，高级席位 15 美元/月；AI for Science 计划每个项目最高提供 5 万美元额度。

### 与现有实验室标准的关系（笔者分析）

MHS 与传统实验室标准的根本区别在于“读者”不同：传统标准假设调用方是工程师编写的程序，MHS 假设调用方是需要“读懂”设备的模型。Anthropic 的公开材料并未将 MHS 与这些标准进行对比，以下为笔者基于公开信息的定位判断：

| 标准 | 设计主体 | 面向谁 | 与 MHS 的关系 |
|---|---|---|---|
| SiLA 2 | 非营利行业联盟（2019 年发布 1.0） | 调度软件与工程师 | 已有自描述特性（FDL 含文字说明与参数约束）和服务发现；MHS 的差异在于以智能体为读者、在设备层强制执行限值、用自然语言生成参考文件，二者可能互补 |
| OPC UA LADS | SPECTARIS 工作组 + OPC 基金会（2023 年发布 1.0） | 实验室与分析仪器 | 依托成熟的 OPC UA 信息模型，但 LADS 本身较新；MHS 更轻量，以原语加自然语言描述为核心 |
| ROS 2 | 机器人开源社区 | 机器人运动与感知 | 运动与感知层仍由 ROS 2 / ros2_control 及控制器固件负责；MHS 位于更上层，负责任务编排 |

## 挑战与展望：瓶颈在物理直觉，变数在治理

MHS 最大的瓶颈不在协议本身，而在模型的物理直觉；最大的不确定性则在于治理与开放节奏。

### 技术局限（官方自述）

- **物理推理薄弱**：Claude 对物理世界的认识来自文本和图像。在 Genentech 的实验中出现气泡报错时，Claude 默认在同一孔位更换参数重试，结果产生了更多气泡；QuEra 的硬件发生故障时，Claude“对装置的理解是程序性的而非物理性的”，无法排障。
- **过度谨慎**：稍有风险便暂停并等待人工确认，实验有时因此停滞一整夜。Anthropic 的立场是“过度谨慎的智能体优于不够谨慎的”。
- **覆盖面有限**：官方称 MHS 尚不支持无编程接口的设备，正与厂商合作内置驱动；CMU 案例以模拟人工操作 GUI 的方式临时接入了无 API 的读板仪，但缺少校验手段。

### 外部争议

- **还不是“标准”**：Kingy AI 指出，目前没有版本化规格、一致性测试、安全威胁模型、认证或发布时间表。生物信息学博主 Keith Robison（Omics! Omics!）以《MHS 到底是什么？我是认真在问》为题，指出规范并未公开披露。
- **模型无关尚未证实**：所有详细案例都使用 Claude。Fortune 称 MHS 也可用于 OpenAI 及开源模型，但目前没有公开的跨模型对比证据。
- **治理空白**：许可协议、所有权与贡献规则均未确定。
- **生物安全与滥用风险**：智能体操作湿实验设备会带来生物安全风险。Anthropic 称正制定“物理安全路线图”以加强防滥用的政策与执行，并将在预览期与合作方建立更多安全评测。

### 展望

1. **短期（6–12 个月）**：内置驱动的厂商增多，驱动库陆续公开；合作方从单点优化走向端到端流程。Genentech 已明确计划建设“科学家设定高层生物学意图、AI 智能体协调物理流程”的自主发现引擎。
2. **中期（1–2 年）**：规范有望开源并附带安全部署指南；治理上可能沿用 MCP“先开源、后捐赠”的中立基金会路径，但因涉及物理安全，节奏很可能更慢；与 SiLA 2、OPC UA 的桥接将是落地关键。
3. **长期**：瓶颈转向模型的物理与化学直觉。Anthropic 自建湿实验室的公开理由是“生物学的最终检验仍在真实实验”；这类闭环实验数据是否会用于训练尚未披露，但很可能成为提升模型物理直觉的关键。

## 结语：对 AI+生物研发的启示

MHS 回答的是“智能体如何操作一台仪器”。AI 驱动的科学发现要回答的问题更大：从一个假设出发，如何自动决定做什么实验、怎样做、做完如何修正假设，并让这个循环持续递归下去。

而类似 INFevo 正在构建的 The Popper Project（TPP），定位是一个递归科学发现（Recursive Scientific Discovery）系统。它覆盖的是这个闭环的全程，而不只是上游的假设生成。MHS 与 TPP 是不同层次的互补关系。MHS 标准化的是“智能体 ↔ 仪器”这一段接口；TPP 的协议层处理的是更上一层的问题——假设如何被编译成可组合、可迁移的实验方案，结果又如何回流修正假设。前者让仪器“可被读懂”，后者让科学问题“可被执行”。

由此有两点启示。第一，协议层会是下一个标准化焦点：当设备接口逐渐统一，瓶颈会上移到“实验方案如何被机器表达、组合与复用”，这一层的开放语言将决定自动化科学的互操作方式。第二，MHS 案例反复暴露的“模型缺乏物理/生物直觉”，恰恰是虚拟细胞模型可以补位之处：在湿实验执行前先做虚拟验证，既能筛掉不值得做的实验，也能为通用智能体提供生物学先验。

TPP 目前已完成假设生成与计算沙盒编排，物理执行层正在补齐——这也是 MHS 这类设备标准对我们的直接意义。

## 参考文献

**一手资料**

1. Previewing the Model Hardware Standard — Anthropic，2026-08-27
2. Expanding support for scientists — Anthropic，2026-08-27
3. Model Hardware Standard 官网
4. Claude Science, an AI workbench for scientists — Anthropic，2026-06-30
5. MCP joins the Agentic AI Foundation — MCP Blog，2025-12-09
6. Holding the light: teaching an AI to lock and tune our quantum computer's lasers — QuEra
7. Tetsuwan × MHS — Tetsuwan Scientific，2026-08-27
8. Building for the Model Hardware Standard — Fastly，2026-09-02

**媒体与分析**

9. Anthropic makes first move into physical AI with universal standard — Fortune，2026-08-27
10. Anthropic wants Claude to run life sciences R&D. Now it is wiring AI agents into the lab. — R&D World，2026-08-28
11. Anthropic Opens a Research Preview of the Model Hardware Standard — MarkTechPost，2026-08-29
12. Anthropic's Model Hardware Standard: What MHS Actually Changes — Kingy AI
13. Model Hardware Standard: What Is It? Seriously, That's What I'm Asking. — Keith Robison，Omics! Omics!
14. Anthropic buys biotech startup Coefficient Bio in $400M deal — TechCrunch，2026-04-03
15. Anthropic launches Claude for Life Sciences — Maginative，2025-10-20
16. Anthropic quietly built a biology lab so Claude can run real experiments — Startup Fortune，2026-09-18
{: start="9"}
