# 操作日志

> 追加式记录：每次 ingest / query / lint 后各记一条。
> 解析技巧：`grep "^## \[" wiki/LOG.md | tail -5`

## [2026-08-10] ingest | 初始化 + 微信文章 × 7

创建知识库骨架并完成首次真实 ingest。

**新建 wiki 结构**：`wiki/INDEX.md`、`wiki/LOG.md`、schema（`AGENTS.md`）、命令（`/wiki-ingest`、`/wiki-query`、`/wiki-lint`）。

**新建实体页（10）**：
- [[华为云 AI Shell]]（来源：我发现了一个免费云服务器，4 核 7G，还自带 DeepSeek）
- [[Void.cloud]]（来源：一键全栈部署，还送独立域名，无需翻墙！Void.cloud 太香了）
- [[Cloudflare Drop]]（来源：这一次，国产彻底暴打 Cloudflare）
- [[花生壳 Drop]]（同上 + Agent 专属的免费域名福利）
- [[花生壳 HSK-CLI]]（来源：Agent 专属的免费域名福利 + 这一次，国产彻底暴打 Cloudflare）
- [[Cloudflare Tunnel]]（来源：Godot+Cloudflare Tunnel内网穿透测试）
- [[Onion OS]]（来源：装一个系统，不用敲一行命令：Onion OS 26.1.0）
- [[Garlic Claw]]（来源：同上）
- [[腾讯云 CloudBase PostgreSQL]]（来源：Agent，你最喜欢的数据库到货了！）
- [[WorkBuddy]]（来源：多篇交叉出现）

**新建概念页（4）**：[[内网穿透]]、[[静态托管]]、[[Agent 基础设施]]、[[国内可达性]]

**新建综述页（1）**：[[AI Agent 时代的免费云基础设施]]

**发现的知识空白 / 待探索**：
- 华为云 AI Shell 保活脚本长期可行性
- Void.cloud 正式定价
- WorkBuddy / Hermes / OpenClaw 横向对比
- 腾讯云 CloudBase 免费额度

## [2026-08-11] ingest | XHS Notes × 2（PCB / 产业链）

首次摄入小红书笔记原始资料（`XHS Notes/知识/`），知识库主题从单一云基础设施扩展到硬件产业链。

**新建概念页（3）**：
- [[PCB]]（来源：一分钟搞懂PCB）
- [[IC 载板]]（来源：一天吃透一条产业链 NO.52 PCB）
- [[产业链]]（来源：一天吃透一条产业链 NO.52 PCB）

**配套接线动作（接通）**：
- `AGENTS.md` raw 源清单补入 `XHS Notes/`（此前未列入）。
- 删除顶层 0 字节悬空文件 `腾讯云 CloudBase PG.md`（wiki 已有同名实体页）。
- 修正 `Horizon/copy-daily.ps1` 与 `.bat` 路径：源 `data/summaries`、目标本工作区 `Horizon-日报`，原指向旧机器 `J:\PERSON\wechat\...`。

**待办**：Horizon 日报管线已接通，运行生成日报后需再 ingest 日报重要条目。

## [2026-08-11] ingest | Horizon 日报 2026-08-10（云端生成 + 本地对齐）

摄入云端 GitHub Actions 生成的 Horizon 日报（`Horizon/Horizon-日报/2026-08-10/_posts/2026-08-10-summary-zh.md`，37→10 条精选）。

**新建实体页（2）**：
- [[OpenClaw]]（来源：Horizon 日报 2026-08-10 #item-tech-news-4）
- [[华为升腾]]（来源：Horizon 日报 2026-08-10 #item-tech-news-7）

**新建概念页（1）**：
- [[人形机器人]]（来源：Horizon 日报 2026-08-10 #item-tech-news-6）

**新建综述页（1）**：
- [[Horizon 日报 2026-08-10]]（当日资讯编译索引）

**更新页面（3）**：
- [[Garlic Claw]] — 加回链 [[OpenClaw]] + 上游自主代理安全风险段落
- [[产业链]] — 补人形机器人（智元/宇树）、图像传感器案例 + 来源
- [[Agent 基础设施]] — 加 [[OpenClaw]]/[[华为升腾]] 案例 + "安全治理"段落

**配套接线动作（接通 + 对齐）**：
- 本地 `Horizon` 仓库 git 元数据曾损坏，已重建并 `git pull` 对齐远程 `main`（`12878bc`），日报落到 `Horizon/Horizon-日报/2026-08-10/`。
- `AGENTS.md` raw 源路径由 `Horizon-日报/` 修正为 `Horizon/Horizon-日报/`（指向真正被 git 跟踪的目录）。
- 移除根目录错位仓库 `Horizon-日报/`（无远程独立 git 仓库，仅含过时 README，路径全错）。

**待办**：后续每日 07:00 云端生成日报后，本地 `git pull` 即自动拿到，再 ingest 重要条目。

## [2026-08-11] ingest | 高考日报 2026-08-11（新增日报源 + 首期生成）

新增与 Horizon 新闻日报平行的「高考每日知识日报」源：AI 每天为数学/语文/英语/物理/化学/地理六科各生成一张知识点卡片。

**新建生成器**：`高考日报/generate_gaokao.py`（复用 Horizon 的 OpenAI 配置；六科各一次调用；输出 `高考日报/<日期>/<日期>-gaokao.md`，文件头带 AI 生成免责声明）。

**首期产出**：`高考日报/2026-08-11/2026-08-11-gaokao.md`（14.6 KB，六科全出，含讲解+例题+答案+解析+易错提醒）。

**新建概念页（1）**：
- [[高考]]（六科每日知识点日报的概念枢纽）

**新建综述页（1）**：
- [[高考日报 2026-08-11]]（当日六科知识点卡片编译索引）

**配套接线动作**：
- `AGENTS.md` raw 源清单补入 `高考日报/`；ingest 触发与每日节奏表（07:30）同步更新。
- 已配置 WorkBuddy 每日自动化：约北京时间 07:30 运行生成器并按 ingest 流程摄入 wiki。

**知识空白 / 待探索**：
- 六科全出 vs 轮换的复习节奏取舍
- AI 生成考点的准确率复核机制（人工抽检 / 多模型交叉）
- 是否按考纲模块系统编排而非随机抽样

