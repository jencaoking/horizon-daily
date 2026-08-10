---
type: entity
created: 2026-08-10
updated: 2026-08-10
sources:
  - "笔记同步助手/2026-08-10/装一个系统，不用敲一行命令：Onion OS 26.1.0.md"
tags: [Linux, 发行版, Xfce, Debian]
---

# Onion OS

## 定位
面向 2GB 内存旧电脑、不懂命令行的非技术用户的 Linux 发行版：macOS 风格桌面 + 系统级 AI 助手，安装全程无命令行。作者：铭荼SCA（bzm2008）。

## 关键能力
- 设计目标：① 2GB 内存流畅（打开 WPS、浏览器、微信不卡）② 界面像 macOS（顶部菜单栏 + 底部 Dock）③ 自带系统级 AI 助手 ④ 安装不需要命令行
- 底层：Debian 12 (Bookworm) + Xfce 4.18 + Picom（glx + dual_kawase 毛玻璃、圆角、柔光阴影）+ Plank Dock
- 26.1.0 修复：桌面配置写入 `/etc/skel`，新用户自动继承主题/壁纸/Dock；`onion-apply-appearance` 服务登录时强制套用，逐显示器适配
- **智能缩放**：自动检测分辨率调整 DPI 与字体（4K→192DPI/14px 字体；1080p→96DPI/11px；768p 以下→9px）
- 预装：WPS Office、微信（deepin-wine）、Firefox ESR、Fcitx5 拼音、应用商店（GNOME Software + Flathub）
- 细节优化：swappiness=10、日志限容 200MB、自动登录 + sudo 免密
- 构建完全脚本化：`git clone https://github.com/bzm2008/onion-os.git` → `sudo ./build_onion_os.sh`（debootstrap → 装桌面 → 配置主题 → 装 Garlic Claw → OTA → 固化 /etc/skel → 打包 ISO 1.4GB）

## 价格 / 限制
- 开源免费；构建脚本与配置开源，ISO 不上传 GitHub（需私信）
- **暂停维护**：缺社区支持、定期安全更新、多语言；Scallion（scallion.uno）生态的一部分

## 相关
- [[Garlic Claw]]（内置 AI 助手）
- [[Agent 基础设施]]
- [[AI Agent 时代的免费云基础设施]]

## 来源
- [[装一个系统，不用敲一行命令：Onion OS 26.1.0]]（铭荼SCA，公众号「带葱铭」，2026-06-14）
