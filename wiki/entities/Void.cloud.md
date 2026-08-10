---
type: entity
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/一键全栈部署，还送独立域名，无需翻墙！Void.cloud 太香了.md"
tags: [部署平台, VoidZero, 免费]
---

# Void.cloud

## 定位
Vite 团队（VoidZero）推出的"全免费全栈"部署平台：用 Vite 生态写项目，敲一行 `void deploy` 自动变全栈应用，免费送 `{项目名}.void.app` 子域名。

## 关键能力
- 真正全栈，一站内置：数据库（D1）、KV 存储、对象存储、用户认证、队列、定时任务（Cron）、AI 推理
- **代码即基础设施**：`import { db } from 'void/db'` 自动创建对应资源，不写 YAML、不点仪表盘
- 自动分配域名，基于 Cloudflare 全球边缘网络，**国内无需翻墙**可稳定访问；可自定义域名
- 支持 React / Vue / Svelte / Solid 等 Vite 生态框架，SSR / SSG / ISR 全支持
- 上手：`npm install -D vite void` → vite.config.ts 加插件 → `void init` → `void deploy`

## 价格 / 限制
- 目前 Private Beta，**免费计划**即可部署全栈应用；数据库、存储、部署基础资源免费额度充足，AI 等计费项可控
- 正式定价未公布（知识空白）

## 相关
- [[静态托管]]
- [[Agent 基础设施]]
- [[国内可达性]]
- [[Cloudflare Drop]]

## 来源
- [[一键全栈部署，还送独立域名，无需翻墙！Void.cloud 太香了]]（空有竹意，公众号，2026-07-13）
