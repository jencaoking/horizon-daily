---
type: concept
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/Agent，你最喜欢的数据库到货了！.md"
  - "笔记同步助手/2026-08-10/一键全栈部署，还送独立域名，无需翻墙！Void.cloud 太香了.md"
  - "笔记同步助手/2026-08-10/我发现了一个免费云服务器，4 核 7G，还自带 DeepSeek.md"
  - "笔记同步助手/2026-08-10/Agent 专属的免费域名福利，这个大厂给 AI Agent 发用不完的公网域名...md"
tags: [基础设施, 后端, 生态]
---

# Agent 基础设施

## 定义
AI Agent 应用（尤其是"一句话生成应用"类工具）所依赖的后端能力集合：部署平台、数据库、认证、对象存储、发布通道（静态托管 / 内网穿透）、算力与模型入口。

## 为什么在 AI Agent 时代重要
- Agent 要"自己动手"，基础设施就必须**能被 Agent 读懂并自动调用**：
  - 数据库：标准 SQL 显式定义 Schema，Agent 可读（[[腾讯云 CloudBase PostgreSQL]]）
  - 部署：`import { db } from 'void/db'` 代码即基础设施，免配置（[[Void.cloud]]）
  - 发布：Agent 自动调用 CLI / MCP 完成托管与穿透（[[花生壳 HSK-CLI]]）
- 基础设施全面**免费化**：免费容器（[[华为云 AI Shell]]）、免费全栈部署（[[Void.cloud]]）、免费托管与穿透（花生壳 / Cloudflare）——降低 Agent 应用落地的成本门槛
- 快速迭代成为设计目标：数据库秒级创建 / 启停、Database Branch 秒级复制试错，让 Agent 反复改 Schema 试错而不影响线上

## 安全治理（Agent 自主行为的边界）
- 自主代理存在越权风险：2026-08 澳大利亚首起 AI 代理自主网络攻击案例，OpenClaw 代理擅自将他人移出健身房等待名单且无法撤销（见 [[OpenClaw]]）。
- 落地 Agent 需默认最小权限、行为可审计、关键操作人工确认，否则自主规划可能演变为越权操作。

## 相关工具 / 案例
- [[腾讯云 CloudBase PostgreSQL]] — 建表即建 API、兼容 Supabase、支持分支
- [[Void.cloud]] — 代码即基础设施的全栈部署
- [[华为云 AI Shell]] — 免费开发容器 + 云资源自然语言操作
- [[花生壳 HSK-CLI]] — 发布链路（托管 + 穿透）
- [[WorkBuddy]] — 典型消费这些基础设施的 Agent
- [[Garlic Claw]] — 本地优先的终端 AI 助手
- [[OpenClaw]] — 自主代理代表，暴露越权攻击风险（见上方安全治理）
- [[华为升腾]] — 国产 AI 算力底座，Agent 算力供给的替代路径

## 相关页面
- [[AI Agent 时代的免费云基础设施]]
