#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高考每日知识日报生成器
========================
每天为 数学 / 语文 / 英语 / 物理 / 化学 / 地理 六科各生成一张知识点卡片
（讲解 + 例题 + 答案 + 解析 + 易错提醒），落盘到：
    高考日报/<日期>/<日期>-gaokao.md

设计要点
--------
- 复用 Horizon 仓库根目录的 .env 里的 OPENAI_API_KEY 与 .venv 里的 openai 包，无需重复配置。
- 模型 / 端点可用环境变量覆盖：GK_MODEL、GK_BASE_URL。
- AI 生成内容仅供学习参考，文件头已带免责声明，正式备考以教材为准。

用法
----
    # 在 Horizon 仓库根目录执行（推荐）：
    .venv/Scripts/python.exe 高考日报/generate_gaokao.py
    # 或在工作区根目录（J:\PERSON\KNOWELGE）执行：
    Horizon/.venv/Scripts/python.exe Horizon/高考日报/generate_gaokao.py 2026-08-11
"""

import os
import sys
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 默认复用 Horizon 仓库根目录的 .env（里面已配置 OPENAI_API_KEY 等）
# 本脚本位于 Horizon/高考日报/，故 .env 在上级目录
HORIZON_ENV = os.path.join(SCRIPT_DIR, "..", ".env")

BASE_URL = os.environ.get("GK_BASE_URL", "https://opencode.ai/zen/v1")
MODEL = os.environ.get("GK_MODEL", "deepseek-v4-flash-free")
API_KEY_ENV = "OPENAI_API_KEY"

SUBJECTS = ["数学", "语文", "英语", "物理", "化学", "地理"]

SYSTEM_PROMPT = """你是经验丰富的高考教研专家，熟悉全国卷及主流教材（人教版等）考纲。
任务：为高三学生生成「每日高考知识点卡片」。

硬性要求：
1. 每次聚焦一个具体、常考、易错的知识点，不要泛泛而谈、不要堆砌目录。
2. 讲解准确、简洁、条理清晰，符合现行高中教材与考纲。
3. 必须配一道典型例题，并给出【答案】与【逐步解析】。
4. 给出 1 条「易错提醒」，点出学生最容易踩的坑。
5. 公式、定理、概念务必正确；若拿不准，明确标注「存疑，需核对教材」，绝不含糊编造。
6. 用简体中文 Markdown 输出。严格以二级标题 `## {科目}`（例如 `## 数学`）作为本节第一个标题开头，
   下方用小节组织：讲解、例题、答案、解析、易错提醒（可用三级标题 `###`）。
7. 不要寒暄、不要开头结尾的客套话，直接输出内容。"""


def load_env(path):
    """把 .env 里的 KEY=VALUE 注入 os.environ（不覆盖已有环境变量）。"""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def beijing_today():
    tz = datetime.timezone(datetime.timedelta(hours=8))
    return datetime.datetime.now(tz).strftime("%Y-%m-%d")


def gen_subject(subject, date_str, client):
    user = (
        f"科目：{subject}\n"
        f"日期：{date_str}\n"
        f"请严格以 `## {subject}` 作为本节第一个二级标题开头，输出该科目今日的知识点卡片。"
    )
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
        temperature=0.3,
        timeout=180,
    )
    return resp.choices[0].message.content.strip()


def main():
    load_env(HORIZON_ENV)
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        print(
            "ERROR: 未找到 OPENAI_API_KEY，请确认 Horizon 仓库根目录的 .env 存在且已配置。",
            file=sys.stderr,
        )
        sys.exit(1)

    from openai import OpenAI

    client = OpenAI(base_url=BASE_URL, api_key=api_key)

    date_str = sys.argv[1] if len(sys.argv) > 1 else beijing_today()
    out_dir = os.path.join(SCRIPT_DIR, date_str)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"{date_str}-gaokao.md")

    sections = []
    for subj in SUBJECTS:
        print(f"  · 生成 {subj} ...", flush=True)
        try:
            text = gen_subject(subj, date_str, client)
        except Exception as e:  # 单科失败不影响其他科
            text = (
                f"## {subj}\n\n"
                f"> 生成本科目内容时出错：{e}\n>\n"
                f"> 可重新运行本脚本（指定同一日期）重试该科目所属的整份日报。"
            )
        sections.append(text)

    header = (
        f"# 高考每日知识 · {date_str}\n\n"
        f"> ⚠️ 本日报由 AI（{MODEL}）自动生成，内容仅供学习参考；"
        f"正式备考请以教材与老师讲解为准，重要结论务必核对。\n\n"
        f"---\n\n"
    )
    body = "\n\n---\n\n".join(sections)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(header + body + "\n")

    print(f"OK 已生成: {out_file}")


if __name__ == "__main__":
    main()
