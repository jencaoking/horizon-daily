@echo off
REM Horizon 日报复制脚本
REM 将生成的日报复制到专用文件夹

set SOURCE_DIR=J:\PERSON\wechat\Horizon\docs
set TARGET_DIR=J:\PERSON\wechat\Horizon-日报

REM 创建目标文件夹（如果不存在）
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

REM 复制日报文件
echo 正在复制日报...
xcopy /E /Y /I "%SOURCE_DIR%\*" "%TARGET_DIR%"

echo 日报已复制到: %TARGET_DIR%
pause
