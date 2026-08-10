---
type: overview
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/我发现了一个免费云服务器，4 核 7G，还自带 DeepSeek.md"
  - "笔记同步助手/2026-08-10/一键全栈部署，还送独立域名，无需翻墙！Void.cloud 太香了.md"
  - "笔记同步助手/2026-08-10/这一次，国产彻底暴打 Cloudflare，免服务器、，国内秒开.md"
  - "笔记同步助手/2026-08-10/装一个系统，不用敲一行命令：Onion OS 26.1.0.md"
  - "笔记同步助手/2026-08-10/Agent 专属的免费域名福利，这个大厂给 AI Agent 发用不完的公网域名...md"
  - "笔记同步助手/2026-08-10/Agent，你最喜欢的数据库到货了！.md"
  - "笔记同步助手/2026-08-10/Godot+Cloudflare Tunnel内网穿透测试.md"
tags: [综述, 免费云资源, Agent生态]
---

# AI Agent 时代的免费云基础设施

## 一页总结
2026 年，AI Agent 生态催生出一批**免费、面向 Agent 自动调用、国内友好**的云基础设施。本期读物（2026-08-10 同步的 7 篇微信文章）恰好勾勒出一条完整的 Agent 应用落地链路：

**开发环境 → 后端能力 → 发布链路**

- 开发环境免费化：[[华为云 AI Shell]]（4核7G 免费容器 + 内置大模型）
- 后端能力 Agent 化：[[腾讯云 CloudBase PostgreSQL]]（建表即建 API）、[[Void.cloud]]（代码即基础设施）
- 发布链路打通：[[静态托管]]（[[花生壳 Drop]] / [[Cloudflare Drop]]）+ [[内网穿透]]（[[花生壳 HSK-CLI]] / [[Cloudflare Tunnel]]）

贯穿始终的关键词：**免费**、**Agent 可自动调用（CLI/MCP）**、**国内可达**（见 [[国内可达性]]）。

## 知识要点
1. **免费竞争白热化**：华为云、腾讯云、花生壳（贝锐）、VoidZero 都在用免费额度圈 Agent 开发者。AI Shell 100W token、Void.cloud Beta 免费、花生壳 Drop/CLI 免费、CloudBase PG 秒级创建。
2. **"代码即基础设施"成为新范式**：`import { db } from 'void/db'`、`void deploy`、建表同时定义身份+权限+自动生成 API——Agent 不需要 YAML 和仪表盘。
3. **发布是最后一公里，也是国内生死线**：静态托管（云端、关机不影响）与内网穿透（依赖本地在线）互补；workers.dev 打不开 → 花生壳已备案域名 + 微信免限制，是同类对比中最具决定性的差异。
4. **为试错设计的数据库**：Database Branch 秒级复制让 Agent 反复改 Schema 不碰线上；闲置自动停算、负载自动扩缩。
5. **本地 AI 的探索**：[[Onion OS]] 把 AI 助手（[[Garlic Claw]]，基于 OpenClaw）做进系统级，端口仅监听本地、API Key 600 权限——本地优先的安全姿态。

## 横向对比

| 平台 | 类型 | 免费 | 国内可用 | 关键限制 |
|---|---|---|---|---|
| [[华为云 AI Shell]] | 开发容器 | ✅（100W token） | ✅ | 6h 有效期、ARM、最多 3 个 |
| [[Void.cloud]] | 全栈部署 | ✅ Beta | ✅（Cloudflare 边缘） | 正式定价未公布 |
| [[Cloudflare Drop]] | 静态托管 | ✅ | ❌（workers.dev 被墙） | 静态只能，不能跑后端 |
| [[花生壳 Drop]] | 静态托管 | ✅ 长期保存 | ✅（已备案） | 静态只能，不能跑后端 |
| [[花生壳 HSK-CLI]] | 托管+穿透 | ✅ | ✅ | 穿透 24h、依赖本地在线 |
| [[Cloudflare Tunnel]] | 内网穿透 | ✅ | ⚠️ 不稳定 | 临时地址、移动端兼容问题 |
| [[腾讯云 CloudBase PostgreSQL]] | 数据库 | ✅（额度待查） | ✅ | 免费额度待补充 |
| [[Onion OS]] | 操作系统 | ✅ 开源 | ✅ | 暂停维护、硬件门槛低 |

## 待探索 / 开放问题
- 华为云 AI Shell 保活脚本能否长期稳定，免费资源会不会收紧（对标 Vercel/Heroku 先例）
- Void.cloud 正式上线后的定价与免费额度变化
- WorkBuddy / Hermes / OpenClaw 等 Agent 工具的横向能力对比（本批来源只有零散观察）
- CloudBase PG 与 Supabase 的实际迁移成本、免费额度
- 国产内网穿透（花生壳）与国际方案（Cloudflare）在稳定性上的长期表现
- 本综述覆盖 3 大基础设施支柱，但缺少**模型与算力层**与**编排/工作流层**的系统资料——待后续 ingest 补全

## 相关页面
- 概念：[[Agent 基础设施]] · [[静态托管]] · [[内网穿透]] · [[国内可达性]]
- 实体：[[华为云 AI Shell]] · [[Void.cloud]] · [[腾讯云 CloudBase PostgreSQL]] · [[花生壳 HSK-CLI]] · [[花生壳 Drop]] · [[Cloudflare Drop]] · [[Cloudflare Tunnel]] · [[Onion OS]] · [[Garlic Claw]] · [[WorkBuddy]]
