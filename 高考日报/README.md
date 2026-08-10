# 高考每日知识日报

每天为 **数学 / 语文 / 英语 / 物理 / 化学 / 地理** 六科各生成一张高考知识点卡片
（讲解 + 例题 + 答案 + 解析 + 易错提醒），落盘到 `高考日报/<日期>/<日期>-gaokao.md`。

与 `Horizon` 新闻日报平行，是本知识库的另一个 raw 源，最终按 `../AGENTS.md` 的 ingest 流程摄入 wiki。

## 运行方式

复用 Horizon 的 Python 环境与密钥（无需重复安装 / 配置）：

```bash
# 在 Horizon 仓库根目录执行（推荐）：
.venv/Scripts/python.exe 高考日报/generate_gaokao.py

# 生成指定日期（补跑 / 重试）：
.venv/Scripts/python.exe 高考日报/generate_gaokao.py 2026-08-11

# 或在工作区根目录（J:\PERSON\KNOWELGE）执行：
Horizon/.venv/Scripts/python.exe Horizon/高考日报/generate_gaokao.py 2026-08-11
```

## 原理

- API 配置读取 Horizon 仓库根目录的 `.env`（即本目录的上一级）里的 `OPENAI_API_KEY`，模型/端点默认：
  - `base_url`: `https://opencode.ai/zen/v1`
  - `model`: `deepseek-v4-flash-free`
- 可用环境变量覆盖：`GK_MODEL`、`GK_BASE_URL`。
- 六科各一次调用，单科失败不中断整份日报。

## 重要提醒

⚠️ 内容为 **AI 自动生成**，可能存在错误。文件头已带免责声明，**正式备考请以教材与老师讲解为准**，重要结论务必核对。

## 自动化

已配置 WorkBuddy 每日自动化（约北京时间 07:30）：自动运行生成器产出当天日报，并按 `AGENTS.md` 摄入 wiki，形成闭环。
如需改为云端（GitHub Actions，类似 Horizon），可参照 `../.github/workflows/daily-summary.yml` 另写一条 workflow。
