# Horizon 日报复制脚本
# 将生成的日报复制到专用文件夹，并按日期组织

$sourceDir = "J:\PERSON\wechat\Horizon\docs"
$targetDir = "J:\PERSON\wechat\Horizon-日报"
$date = Get-Date -Format "yyyy-MM-dd"
$dailyDir = Join-Path $targetDir $date

# 创建目标文件夹（如果不存在）
if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force
}

# 创建日期文件夹
if (-not (Test-Path $dailyDir)) {
    New-Item -ItemType Directory -Path $dailyDir -Force
}

# 复制日报文件
Write-Host "正在复制日报到: $dailyDir"
Copy-Item -Path "$sourceDir\*" -Destination $dailyDir -Recurse -Force

# 创建今日日报索引
$indexContent = @"
# Horizon 日报 - $date

## 今日概览

生成时间: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## 文件列表

"@

# 列出所有复制的文件
$files = Get-ChildItem -Path $dailyDir -Recurse -File
foreach ($file in $files) {
    $relativePath = $file.FullName.Substring($dailyDir.Length + 1)
    $indexContent += "- [$relativePath]($relativePath)`n"
}

# 保存索引文件
$indexContent | Out-File -FilePath (Join-Path $dailyDir "README.md") -Encoding UTF8

Write-Host "✅ 日报已复制到: $dailyDir"
Write-Host "📄 索引文件: $dailyDir\README.md"
Write-Host "📊 共复制 $($files.Count) 个文件"
