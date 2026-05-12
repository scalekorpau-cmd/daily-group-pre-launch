# Create empty repo first: https://github.com/new?name=daily-group-pre-launch
# (Public or Private — recommend Private if manifest contains operational details you prefer off public GitHub.)
#
# powershell -ExecutionPolicy Bypass -File "C:\Users\DELL\daily-group-pre-launch\PUSH_TO_GITHUB_ONCE.ps1"

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
git branch -M main
$url = "https://github.com/scalekorpau-cmd/daily-group-pre-launch.git"
if (git remote get-url origin 2>$null) { git remote set-url origin $url } else { git remote add origin $url }
git push -u origin main
