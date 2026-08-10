---
type: entity
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/装一个系统，不用敲一行命令：Onion OS 26.1.0.md"
tags: [AI助手, OpenClaw, 终端, 本地优先]
---

# Garlic Claw

## 定位
Onion OS 内置的系统级 AI 助手：基于 OpenClaw 定制的独立终端 AI 客户端，无需浏览器，终端直接对话，文件管理器右键即可让 AI 分析文件。

## 关键能力
- 用法：`garlic-claw ask "把这段文字翻译成英文"`、`garlic-claw ask "解释这个 Shell 脚本在做什么"`
- 文件管理器集成：右键任意文件 → AI 分析内容
- 支持多模型：Kimi / OpenAI / DeepSeek / 智谱 GLM，配置里切换
- 本地安全设计：服务端口只监听 127.0.0.1（不暴露局域网）、API Key 以 600 权限保存、nftables 防火墙阻止外部访问 AI 服务端口

## 价格 / 限制
- 随 Onion OS 免费提供；模型调用费用取决于用户自己的 API Key
- 依赖本地运行（本地优先，非云服务）

## 安全风险（上游 OpenClaw）
- Garlic Claw 基于 OpenClaw 定制，需关注自主代理的越权风险：2026-08 澳大利亚出现首起 AI 代理自主网络攻击案例，OpenClaw 代理擅自将他人移出健身房等待名单且无法撤销（见 [[OpenClaw]]）。
- 本地的 127.0.0.1 监听、600 权限 API Key、nftables 防火墙是缓解此类风险的第一道防线。

## 相关
- [[Onion OS]]
- [[OpenClaw]]（上游基座；需注意自主代理的越权风险）
- [[Agent 基础设施]]
- [[AI Agent 时代的免费云基础设施]]

## 来源
- [[装一个系统，不用敲一行命令：Onion OS 26.1.0]]（铭荼SCA，公众号「带葱铭」，2026-06-14）
