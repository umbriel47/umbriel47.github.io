---
layout: post
title: "AI 资本开支的 100 美元，最后变成了谁的利润？"
date: 2026-10-04 08:37:00 +0800
lang: zh
ref: who-profits-from-ai-capex
tags: [science]
wide: true
wechat_url: "https://mp.weixin.qq.com/s/6Ph3sB2uH7urAQxdrXVw4A"
description: "a16z Growth 引用的一张估算图把 100 美元 AI 资本开支拆到供应链各层。用公开财报核对后，支出份额大体可信，但利润高度集中：芯片拿走约一半支出，却可能占到整条链毛利的六到七成，而存储正在挤进这一层的顶部。"
---

2026 年，美国四家最大的云厂商合计计划投入约 7250 亿美元资本开支，比 2025 年的约 4100 亿美元增长七成以上（Tom's Hardware, 2026-04-30[\[1\]](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)）；英伟达在 8 月的电话会上给出的口径更大：前五大云厂商 2026 年资本开支接近 8000 亿美元，2027 年约 1.3 万亿美元（英伟达 2027 财年二季度电话会记录[\[2\]](https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)）。这么大一笔钱流进供应链，常见的讨论停留在“谁拿到了订单”。这篇想追问下一步：**订单变成收入之后，利润留在了哪一层？**我的判断是，支出份额和利润份额之间存在明显的错位，而且这种错位在 2026 年正在向存储一侧移动。

## 一张估算图，以及它能回答什么

讨论的起点是 a16z Growth 近期传播的一张桑基图，标题为“Following The AI Capex Money”。它把一笔假想的 100 美元 AI 资本开支拆到供应链各层，来源标注为法国巴黎银行（BNP Paribas）股票研究，日期为 2026 年 8 月，并注明是“高层级估算，随成本与供需快速变化而调整”。

<figure>
  {%- include charts/ai-capex/zh/fig1.svg -%}
  <figcaption>图 1 ｜ 100 美元 AI 资本开支在供应链上的示意性拆分（估算，非实测） · 来源：数据引自 BNP Paribas Equity Research（2026 年 8 月），经 a16z Growth 图表转引，一目半重新绘制</figcaption>
</figure>

按图中数字，100 美元里：半导体芯片 50 美元（其中加速器 25、存储 15、CPU 及其他芯片与服务器生产 10），网络设备 15 美元（光模块 5.5、交换机 4.5、网络处理器 3、线缆 2），电力 20 美元（并网与自备发电 10、配电 6.5、场内电力布线 3.5），冷却 7.5 美元，厂房与建设 7.5 美元。另有一支从芯片层引出的晶圆厂设备（WFE）8 美元。下文把这张图当作一份券商估算来核对，而不是当作数据。

这张图回答的是“钱首先付给了谁”。它没有回答另一个问题。

支出份额与价值获取：支出份额指一笔资本开支中流向某一环节的比例，对应的是该环节的收入。价值获取指这部分收入在扣除成本后留下多少利润。两个环节可以拿到同样多的订单，却留下截然不同的利润。

## 逐层核对：芯片这一半

**加速器与系统厂商。**英伟达截至 2026 年 7 月 26 日的季度收入 962 亿美元，其中数据中心 890 亿美元，毛利率 75.0%，GAAP 营业利润 637 亿美元，营业利润率约 66%（英伟达新闻稿[\[3\]](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm)）。博通同期 AI 半导体收入 167 亿美元，按其新闻稿财务表推算的非 GAAP 毛利率约 75%（博通新闻稿[\[4\]](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm)）。加速器这一层的收入规模和毛利率，都处在整条链的顶端。

这里与图有一处值得注意的出入。2025 年 8 月，黄仁勋在电话会上说，一座 1 吉瓦 AI 工厂造价约 500 亿至 600 亿美元，其中英伟达约占 350 亿美元（英伟达 2026 财年二季度电话会记录[\[5\]](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/NVDA-Q2-2026-Earnings-Call-27-August-2025-5_00-PM-ET.pdf)）；2026 年 8 月的电话会进一步称，每吉瓦的英伟达含量从 Hopper 的约 180 亿美元、Blackwell 的约 250 亿美元，升至 Vera Rubin 的约 400 亿美元。按这个口径，英伟达一家就占一座 AI 工厂的六到七成，高于图中“加速器 25 美元”。差异大部分来自定义：英伟达的收入包含它代购并封装进 GPU 的 HBM、Grace/Vera CPU、NVLink 交换芯片和网卡，而图把这些分别计入存储、CPU 和网络。即便如此，两种口径并排看仍提示，系统厂商通过打包销售，实际收拢的份额可能比按芯片类别拆分的图更大。也要看到，这个数字出自卖方本人。

**存储。**这是 2026 年变化最大的一层。SK 海力士二季度收入 79.3 万亿韩元，营业利润 60.5 万亿韩元，营业利润率 76%（SK 海力士 2Q26 业绩[\[6\]](https://www.storagenewsletter.com/2026/07/30/sk-hynix-fiscal-2q26-financial-results/)）。美光截至 2026 年 9 月 3 日的季度收入 542 亿美元，GAAP 毛利率 86.8%，并指引下一季度收入约 615 亿美元、毛利率约 86%（美光新闻稿[\[7\]](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm)）。换句话说，最近一个季度，两家存储厂商的利润率已经高于英伟达。

成本端的证据指向同一方向。英伟达在电话会上说，存储涨价幅度“超出此前预期，明年还会更高”，并把下一季度毛利率指引下调到 74%。微软 CFO 把 2026 年资本开支中约 250 亿美元归因于存储与零部件涨价，Meta 也给出类似说明（Tom's Hardware[\[1\]](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)）。如果这些说法成立，图中“存储 15 美元”在 2026 年下半年可能偏低；至少可以说，存储正在从加速器那里分走一部分利润。

**CPU、其他芯片与服务器生产。**这 10 美元内部差异极大。CPU 和定制芯片的毛利率较高，而整机组装毛利很薄：鸿海 2026 年二季度收入同比增长 41%，毛利率仅 6.12%，营业利润率 3.75%（鸿海 2Q26 业绩[\[8\]](https://iconnect007.com/article/151169/foxconn-announces-q2-2026-financial-results/151166/ein)）。服务器出货量最大的环节，恰恰是利润率最低的环节之一。

**晶圆代工与设备：第二层的钱。**台积电不在图上，但它是加速器的上游。二季度台积电毛利率 67.7%，营业利润率 60.3%，高性能计算占收入 66%，全年资本开支上调至 600 亿至 640 亿美元（台积电 2Q26 业绩[\[9\]](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm)；电话会记录[\[10\]](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf)）。台积电的资本开支，又成为设备商的收入：ASML 二季度毛利率 54.0%，全年收入指引 430 亿至 450 亿欧元（ASML 新闻稿[\[11\]](https://investor.asml.com/news-releases/news-release-details/q2-2026-financial-results)）；SEMI 预计 2026 年全球 WFE 销售额 1439 亿美元，同比增长 23%（SEMI, 2026-07-14[\[12\]](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports)）。

这一点决定了怎么读图中的 WFE 8 美元：它不是 100 美元之外的额外支出，而是芯片厂商用收入支付的再投资，属于第二层流动，不能与第一层相加。

## 逐层核对：网络、电力、冷却与建筑

**网络。**图中网络占 15 美元，内部毛利率分化明显。Arista 二季度收入 30.4 亿美元，非 GAAP 毛利率 63.4%，营业利润率 49.9%（Arista 新闻稿[\[13\]](https://finviz.com/news/377054/arista-networks-inc-reports-second-quarter-2026-financial-results)）；光模块厂商 Coherent 截至 6 月的季度收入 20.5 亿美元，非 GAAP 毛利率 40.2%（Coherent 新闻稿[\[14\]](https://www.sec.gov/Archives/edgar/data/0000820318/000119312526346860/d128030dex991.htm)）。同属网络，交换机和网络芯片的利润率接近半导体，光模块明显更低，线缆更接近制造业。

**电力、冷却与建筑。**这三项在图中合计 35 美元，占三分之一以上。外部数据大体支持这个量级：Cushman & Wakefield 2026 年成本指南给出的美国与加拿大新建数据中心平均造价为每兆瓦 1760 万美元，不含芯片与 GPU，较 2024 年四季度上涨 21%，电力基础设施是最大单项，约占 21%（Cushman & Wakefield, 2026-09-03[\[15\]](https://finviz.com/news/388803/cushman-wakefield-releases-2026-data-center-development-cost-guide-citing-21-rise-in-per-mw-construction-costs)）。若 1 吉瓦总造价按 500 亿至 600 亿美元计，不含芯片的部分约 176 亿美元，占三成左右，与图中 35% 接近。需要说明，图中“并网与自备发电 10 美元”可能部分落在 Cushman 的统计口径之外，两者不能逐项对齐。

利润率是另一回事。冷却与配电龙头 Vertiv 二季度收入 32.7 亿美元，调整后营业利润率 22.6%，全年指引 23.3% 至 24.3%（Vertiv 新闻稿[\[16\]](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm)）。这在工业企业中已属很高，GE Vernova 二季度订单也同比有机增长 88%（Quartz[\[17\]](https://qz.com/ge-vernova-2026-revenue-guidance-second-quarter-earnings-072226)），但与半导体相比仍低一个量级。建筑施工环节的利润率更薄，我没有找到针对数据中心总包的可靠公开数据，下文按低双位数毛利率估计。

## 从花钱到赚钱：按毛利重算一遍

把以上数据合在一起，可以做一个粗略换算：用图中各层的支出，乘以该层代表性公司最近一个季度的毛利率，得到每 100 美元在各层留下的毛利。假设如下：加速器 75%（英伟达、博通），存储 80%（美光与 SK 海力士之间取偏保守值），CPU 及服务器生产 25%（高毛利芯片与 6% 左右的组装混合），网络 50%，电力 25%，冷却 35%，建筑 12%。后三项缺少直接可比的毛利率披露，是我的估计。

按此计算，100 美元支出大约留下 49 美元毛利。其中加速器约 19 美元，存储约 12 美元，CPU 与服务器约 2.5 美元，网络约 7.5 美元，电力约 5 美元，冷却约 2.6 美元，建筑约 0.9 美元。

<figure>
  {%- include charts/ai-capex/zh/fig2.svg -%}
  <figcaption>图 2 ｜ 支出份额与估算毛利份额对比：芯片拿走一半支出，却占约三分之二毛利；电力、冷却与建筑占三成多支出，只占不到两成毛利 · 来源：一目半根据图 1 与各公司财报估算</figcaption>
</figure>

换成份额看，错位很清楚。加速器、存储与 CPU 合计占支出的 50%，却占毛利的约 67%；电力、冷却与建筑合计占支出的 35%，只占毛利的约 17%。仅加速器与存储两项就以 40% 的支出拿到约六成毛利。

<figure>
  {%- include charts/ai-capex/zh/fig3.svg -%}
  <figcaption>图 3 ｜ 供应链代表性公司最近一个季度毛利率（各公司财季截止日不同，详见正文） · 来源：各公司新闻稿，一目半整理</figcaption>
</figure>

这个结果对假设并不特别敏感。把电力和冷却的毛利率各上调 10 个百分点，芯片的毛利份额仍在六成以上。真正敏感的是存储：存储毛利率历来随周期大幅波动，若回落到四成上下，整条链的毛利会减少约 6 美元，芯片份额随之降到六成左右。换言之，本文最确定的结论是“利润集中在芯片”，最不确定的是“存储能在这一层停留多久”。

> AI 资本开支的支出图谱是一张宽图，利润图谱却是一张窄图：钱流向数十个环节，利润主要留在少数几种芯片里。

## 图与公开数据不一致的地方

核对过程中，有三处值得读者留意。

第一，图内部有一处算术不一致。WFE 节点标注为 8 美元，但它引出的五个分支合计为 18 美元（沉积 2、光刻 12、刻蚀 1、检测 1、封装及其他 2）。如果光刻实为 2 美元，五项恰好合计 8 美元，因此较可能是标注错误，但我无法确认。另外，按 Yole 对 2023 年的统计，WFE 中图形化设备约占 30%，沉积约 26% 到 27%，刻蚀与清洗约 19%（Yole Group[\[18\]](https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/)），图中刻蚀仅占八分之一，比例偏低。图的来源行中“BNP Paribas”也拼作了“BNP Panbas”。

第二，系统厂商的份额。如前所述，英伟达自己的口径意味着它单家占一座 AI 工厂的六到七成，高于图中按芯片类别拆分得出的印象。口径不同可以解释大部分差异，但不是全部。

第三，存储的份额与利润。图的日期是 2026 年 8 月，可能已部分反映存储涨价；而英伟达、微软在 7 至 8 月的表态都显示，存储成本仍在上行。图中 15 美元更像一个时点估计，而不是稳态。

## 最强的反方：毛利不是全部的账

这套换算有几处必须正面承认的局限。

毛利率不等于经济利润。芯片设计公司的研发投入巨大，代工与存储厂商每年要把大量收入重新投入产能：台积电 2026 年资本开支 600 亿美元以上，存储厂商也在扩产。若按资本回报率而非毛利率计算，各层之间的差距会缩小，存储尤其如此，因为它的高毛利往往出现在供给紧张、尚未大规模扩产的窗口期。

最终的价值获取者也可能不在供应链上，而在买方。AWS 二季度营业利润率 39.4%，但据一份基于财报的分析，亚马逊过去十二个月自由现金流已转为约负 76 亿美元（beancount.io 分析[\[19\]](https://beancount.io/blog/2026/07/31/amazon-fy2026-q2-earnings-analysis)）。云厂商今天的支出，是在购买未来多年的算力收入。这些资产的折旧年限、利用率和定价，决定了 7000 多亿美元最终是供应链的利润，还是买方的回报。英伟达称一吉瓦 AI 工厂每年租金约等于其造价（24/7 Wall St. 转述[\[20\]](https://247wallst.com/investing/2026/09/24/nvidias-ceo-says-a-1-gigawatt-ai-factory-rents-for-50-billion-a-year-as-much-as-it-costs-to-build/)），这个说法同样出自卖方，尚未见独立核实。

最后，本文混用了截止日不同的财季，英伟达截至 7 月下旬，美光截至 9 月初，Coherent 截至 6 月底。在价格快速变化的年份，这会带来误差。

## 仍然开放的问题

第一，存储的超额利润能持续多久？它取决于 HBM 扩产节奏，以及加速器厂商能否把成本转嫁给云厂商。

第二，系统厂商的打包能力会不会继续扩张？每吉瓦英伟达含量从 180 亿美元升至 400 亿美元的说法若兑现，网络、CPU 乃至部分冷却与供电的价值，可能进一步被纳入单一供应商的报价。

第三，电力会不会从“支出大户”变成“利润大户”？当并网排队和发电设备交付成为约束时，稀缺性可能把部分议价能力转移给电力设备商和拥有并网资源的开发商。目前的利润率数据还没有显示这种转移。

## 要点

1. 图 1 回答的是钱付给了谁，不是利润留在哪里；WFE 属于第二层流动，不能与第一层相加。
2. 按代表性毛利率换算，芯片约占支出的一半、毛利的三分之二；电力、冷却与建筑占支出三成多、毛利不到两成。
3. 2026 年最大的变量是存储：最近一个季度存储厂商利润率已高于英伟达，图中的存储份额可能偏低。

跟着资本开支走，能看到订单流向何处；跟着毛利率走，才能看到这轮建设的利润究竟落在谁手里。

## 参考资料

1. <https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion>
2. <https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf>
3. <https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm>
4. <https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm>
5. <https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/NVDA-Q2-2026-Earnings-Call-27-August-2025-5_00-PM-ET.pdf>
6. <https://www.storagenewsletter.com/2026/07/30/sk-hynix-fiscal-2q26-financial-results/>
7. <https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm>
8. <https://iconnect007.com/article/151169/foxconn-announces-q2-2026-financial-results/151166/ein>
9. <https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm>
10. <https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf>
11. <https://investor.asml.com/news-releases/news-release-details/q2-2026-financial-results>
12. <https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports>
13. <https://finviz.com/news/377054/arista-networks-inc-reports-second-quarter-2026-financial-results>
14. <https://www.sec.gov/Archives/edgar/data/0000820318/000119312526346860/d128030dex991.htm>
15. <https://finviz.com/news/388803/cushman-wakefield-releases-2026-data-center-development-cost-guide-citing-21-rise-in-per-mw-construction-costs>
16. <https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm>
17. <https://qz.com/ge-vernova-2026-revenue-guidance-second-quarter-earnings-072226>
18. <https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/>
19. <https://beancount.io/blog/2026/07/31/amazon-fy2026-q2-earnings-analysis>
20. <https://247wallst.com/investing/2026/09/24/nvidias-ceo-says-a-1-gigawatt-ai-factory-rents-for-50-billion-a-year-as-much-as-it-costs-to-build/>
