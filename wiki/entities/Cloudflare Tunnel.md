---
type: entity
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/Godot+Cloudflare Tunnel内网穿透测试.md"
tags: [Cloudflare, 内网穿透, 游戏开发]
---

# Cloudflare Tunnel

## 定位
Cloudflare 的免费内网穿透服务：`cloudflared` 一键把本地服务暴露到公网，生成 `https://xxx.trycloudflare.com` 临时地址，无需服务器、无需公网 IP。

## 关键能力
- 命令：`cloudflared tunnel --url http://127.0.0.1:<端口>`，输出一串 trycloudflare.com 临时地址
- 局域网 / 任何网络环境下打开浏览器即可访问
- Windows 安装：官网 exe 可能被系统拦截，改用 `winget` 安装成功（版本 2026.7.3）
- 与 [[花生壳 HSK-CLI]] 同类能力，是 Cloudflare 版本的"打洞"工具

## 实战经验（Godot 4.7 Web 导出 + 穿透）
1. 编辑器设置：导出 Web → HTTP Host 改 `0.0.0.0` + 勾选 TLS；渲染器选 Compatibility
2. Godot 内置"在浏览器中运行"在某种配置下会卡住 → 改用：项目导出后 `python -m http.server 8000` 起服务
3. 再另开 cmd：`cloudflared tunnel --protocol http2 --url http://127.0.0.1:8000` 穿透
4. 注意：两个 cmd 窗口常驻、以管理员运行、浏览器标签保持打开，否则服务停止

## 价格 / 限制
- 免费；临时地址无固定域名
- 实测不稳定（作者考虑国产替代）
- 移动端穿透存在问题（疑似手机浏览器兼容性，需要配置 https）

## 相关
- [[内网穿透]]
- [[花生壳 HSK-CLI]]
- [[国内可达性]]

## 来源
- [[Godot+Cloudflare Tunnel内网穿透测试]]（苔，公众号「苔之踪」，2026-08-09）
