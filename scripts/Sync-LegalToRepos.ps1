<#
.SYNOPSIS
  Clone each configured GitHub repo, inject static legal HTML (terms, privacy, cookies), commit, push.

.DESCRIPTION
  Requires: Git on PATH, GitHub CLI (gh) with `gh auth login` completed.
  Configure repos-legal-manifest.json (copy from repos-legal-manifest.example.json).
  Set "skip": false only for repos that serve static files from "relativeTarget" (e.g. public/).

  This is a pragmatic bulk approach. Next.js App Router sites usually need custom pages — mark skip true
  and handle in that repo (like TradesBook React routes).
#>
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$LegalDir = Join-Path $Root "..\01-universal-standards\legal"
$ManifestPath = Join-Path $Root "repos-legal-manifest.json"
$ExamplePath = Join-Path $Root "repos-legal-manifest.example.json"
$WorkRoot = Join-Path ([System.IO.Path]::GetTempPath()) "daily-group-legal-sync"

$TemplateMap = @{
  "terms.html"    = "TERMS_OF_SERVICE_TEMPLATE.html"
  "privacy.html"  = "PRIVACY_POLICY_TEMPLATE.html"
  "cookies.html"  = "COOKIES_POLICY_TEMPLATE.html"
}

function Test-GhAuth {
  $ghExe = $null
  $cmd = Get-Command gh -ErrorAction SilentlyContinue
  if ($cmd) { $ghExe = $cmd.Source }
  elseif (Test-Path "${env:ProgramFiles}\GitHub CLI\gh.exe") { $ghExe = "${env:ProgramFiles}\GitHub CLI\gh.exe" }
  elseif (Test-Path "${env:LocalAppData}\Programs\GitHub CLI\gh.exe") { $ghExe = "${env:LocalAppData}\Programs\GitHub CLI\gh.exe" }
  if ($ghExe) {
    & $ghExe auth status 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
      throw "GitHub CLI not logged in. Run: gh auth login   (see scripts\LEGAL_SYNC_README.txt)"
    }
    return
  }
  $git = Get-Command git -ErrorAction SilentlyContinue
  if (-not $git) { throw "Git not found on PATH. Install Git for Windows." }
  Write-Warning "GitHub CLI (gh) not found - skipping gh auth check. Ensure git push works (SSH key or credential manager)."
}

function Apply-Placeholders([string]$Content, [psobject]$Placeholders) {
  $out = $Content
  foreach ($p in $Placeholders.PSObject.Properties) {
    $key = $p.Name
    $val = [string]$p.Value
    $out = $out -replace [regex]::Escape("[$key]"), $val
  }
  if ($out -match '\[[A-Z0-9_]+\]') {
    Write-Warning "Unresolved [PLACEHOLDER] tokens remain in output; check manifest placeholders for this repo."
  }
  return $out
}

function Sync-OneRepo($entry) {
  if ($entry.skip -eq $true) {
    Write-Host "[SKIP] $($entry.id)" -ForegroundColor DarkGray
    return
  }
  $id = $entry.id
  if (-not $id -or -not $entry.gitUrl) { throw "Manifest entry missing id or gitUrl" }
  $dest = Join-Path $WorkRoot $id
  $branch = if ($entry.branch) { $entry.branch } else { "main" }
  $rel = if ($entry.relativeTarget) { $entry.relativeTarget } else { "public" }
  $msg = if ($entry.commitMessage) { $entry.commitMessage } else { "Add static legal pages (privacy, terms, cookies)" }

  if (-not (Test-Path $dest)) {
    Write-Host "[CLONE] $($entry.gitUrl) -> $dest"
    git clone --depth 1 -b $branch $entry.gitUrl $dest
  } else {
    Write-Host "[PULL] $id"
    git -C $dest fetch origin $branch
    git -C $dest checkout $branch
    git -C $dest pull origin $branch
  }

  $targetDir = Join-Path $dest $rel
  if (-not (Test-Path $targetDir)) {
    Write-Host "  Creating missing folder: $targetDir" -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
  }

  foreach ($outName in $TemplateMap.Keys) {
    $srcName = $TemplateMap[$outName]
    $srcPath = Join-Path $LegalDir $srcName
    if (-not (Test-Path $srcPath)) { throw "Missing template: $srcPath" }
    $raw = Get-Content -Path $srcPath -Raw -Encoding UTF8
    $filled = Apply-Placeholders $raw $entry.placeholders
    $outPath = Join-Path $targetDir $outName
    Set-Content -Path $outPath -Value $filled -Encoding UTF8
    Write-Host "  wrote $outName"
  }

  git -C $dest add -- "$rel/terms.html" "$rel/privacy.html" "$rel/cookies.html"
  $st = git -C $dest status --porcelain
  if (-not $st) {
    Write-Host "[NO CHANGES] $id (files identical?)" -ForegroundColor Yellow
    return
  }
  git -C $dest commit -m $msg
  Write-Host "[PUSH] $id"
  git -C $dest push origin $branch
}

# --- main ---
Test-GhAuth

if (-not (Test-Path $ManifestPath)) {
  Write-Host "Creating $ManifestPath from example. Edit it, set skip:false, then re-run." -ForegroundColor Yellow
  Copy-Item $ExamplePath $ManifestPath
  exit 1
}

New-Item -ItemType Directory -Force -Path $WorkRoot | Out-Null
$list = Get-Content $ManifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($list -isnot [System.Array]) { $list = @($list) }

foreach ($e in $list) {
  Write-Host "`n=== $($e.id) ===" -ForegroundColor Cyan
  Sync-OneRepo $e
}

Write-Host "`nDone. Clones left under: $WorkRoot (delete when finished if you want)" -ForegroundColor Green
