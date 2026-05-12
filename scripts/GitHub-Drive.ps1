#Requires -Version 5.1
<#
.SYNOPSIS
  Small "GitHub drive" — repeatable git/gh actions outside Cursor's chat UI.
.DESCRIPTION
  Dot-source this file:  . .\GitHub-Drive.ps1
  Then use: ghstatus, ghrepos, Push-RepoMain, New-GitHubRepoAndPush
#>

$script:GhExe = $null
foreach ($c in @(
        "${env:ProgramFiles}\GitHub CLI\gh.exe",
        (Get-Command gh -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source)
    )) {
    if ($c -and (Test-Path -LiteralPath $c)) { $script:GhExe = $c; break }
}

function Test-GitHubAuth {
    if (-not $script:GhExe) {
        Write-Warning "GitHub CLI not found. Install: winget install GitHub.cli"
        return $false
    }
    $env:Path = "$(Split-Path $script:GhExe -Parent);$env:Path"
    gh auth status 2>&1 | Out-Host
    return ($LASTEXITCODE -eq 0)
}

function Get-GitHubTokenPresent {
    return [bool]$env:GITHUB_TOKEN -or [bool]$env:GH_TOKEN
}

function ghstatus {
    Write-Host "=== Token env (set = yes, empty = no) ===" -ForegroundColor Cyan
    Write-Host "GITHUB_TOKEN: $(if ($env:GITHUB_TOKEN) { 'set' } else { 'empty' })"
    Write-Host "GH_TOKEN:     $(if ($env:GH_TOKEN) { 'set' } else { 'empty' })"
    Write-Host ""
    if (-not $script:GhExe) { Write-Warning "gh not installed"; return }
    Test-GitHubAuth
}

function Get-GitHubRepos {
    if (-not $script:GhExe) { Write-Warning "gh not installed"; return }
    $env:Path = "$(Split-Path $script:GhExe -Parent);$env:Path"
    gh repo list --limit 80
}

function Push-RepoMain {
    param(
        [Parameter(Mandatory = $true)]
        [string] $RepoRoot
    )
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot ".git"))) {
        throw "Not a git repo: $RepoRoot"
    }
    Push-Location $RepoRoot
    try {
        git status -sb
        $branch = (git rev-parse --abbrev-ref HEAD).Trim()
        if ($branch -ne "main") { git branch -M main 2>$null }
        git push -u origin main
    }
    finally {
        Pop-Location
    }
}

function New-GitHubRepoAndPush {
    <#
    Creates an EMPTY repo on GitHub (requires gh auth or token), adds origin, pushes main.
    Run from folder that already has git init + commits.
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string] $RepoRoot,
        [Parameter(Mandatory = $true)]
        [string] $RepoName,
        [string] $Description = "",
        [switch] $Private
    )
    if (-not $script:GhExe) { throw "Install GitHub CLI first." }
    $env:Path = "$(Split-Path $script:GhExe -Parent);$env:Path"
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot ".git"))) {
        throw "Not a git repo: $RepoRoot"
    }
    $vis = if ($Private) { "--private" } else { "--public" }
    Push-Location $RepoRoot
    try {
        git branch -M main 2>$null
        $args = @("repo", "create", $RepoName, "--source=.", "--remote=origin", "--push", $vis)
        if ($Description) { $args += "--description"; $args += $Description }
        & gh @args
    }
    finally {
        Pop-Location
    }
}

function Open-GitHubRepo {
    param([Parameter(Mandatory = $true)][string] $Slug)  # e.g. scalekorpau-cmd/daily-group-pre-launch
    Start-Process "https://github.com/$Slug"
}

Write-Host "GitHub-Drive loaded. Commands: ghstatus, Get-GitHubRepos, Push-RepoMain, New-GitHubRepoAndPush, Open-GitHubRepo" -ForegroundColor Green
Write-Host "Example:  Push-RepoMain -RepoRoot 'C:\Users\DELL\daily-group-pre-launch'" -ForegroundColor DarkGray
Write-Host "Example:  Open-GitHubRepo -Slug 'scalekorpau-cmd/daily-group-pre-launch'" -ForegroundColor DarkGray
