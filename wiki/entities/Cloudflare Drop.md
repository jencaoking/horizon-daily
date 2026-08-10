---
type: entity
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/这一次，国产彻底暴打 Cloudflare，免服务器、，国内秒开.md"
tags: [Cloudflare, 静态托管]
---

# Cloudflare Drop

## 定位
Cloudflare 推出的轻量静态文件发布工具：把 HTML、CSS、JS、图片拖进去，直接生成公网链接，一键分享。

## 关键能力
- 拖拽 HTML / 压缩包 / 整个网页文件夹即可发布
- 发布后部署到 workers.dev 域名
- 适合 WorkBuddy / Claude Code / Codex 等 Agent 生成的静态网页一键上公网
- 注意：网页里的 JavaScript 实际在**访问者的浏览器**执行，不能用作前端转发

## 价格 / 限制
- 免费
- **国内打不开**：最终部署在 workers.dev，该地址在国内无法访问，微信分享受限
- 只能静态托管，不能跑 Node.js / Python / 数据库等后端服务
- 上传需文件夹或压缩包（不支持单个 html）

## 相关
- [[静态托管]]
- [[花生壳 Drop]]（国产替代，国内可访问）
- [[国内可达性]]
- [[Agent 基础设施]]

## 来源
- [[这一次，国产彻底暴打 Cloudflare，免服务器、，国内秒开]]（可爱的小Cherry，公众号，2026-07-28）
