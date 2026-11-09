# Pre-publish scan: looks for environment URLs, GUIDs, secrets and non-example emails.
# Usage: pwsh scripts/prepublish-scan.ps1   (run from the repo root)
$root = Resolve-Path (Join-Path $PSScriptRoot '..')
$patterns = [ordered]@{
  'Dynamics/Power Platform URL' = '[a-z0-9-]+\.(crm\d*\.dynamics\.com|api\.crm\d*\.dynamics\.com|powerapps\.com|powerplatform\.com)'
  'make.* environment link'     = 'environments/[0-9a-fA-F-]{36}'
  'GUID'                        = '\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'
  'onmicrosoft tenant'          = '[a-z0-9-]+\.onmicrosoft\.com'
  'Secret-like keyword'         = '(?i)(client_?secret|password|apikey|api_key|accountkey|sharedaccesssignature|bearer\s+[a-z0-9._-]{20,})\s*[:=]'
  'Email not on example.com'    = '[A-Za-z0-9._%+-]+@(?!example\.com|users\.noreply\.github\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
}
$files = Get-ChildItem -Path $root -Recurse -File |
  Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.FullName -notmatch 'prepublish-scan\.ps1$' -and $_.Extension -notin '.png','.jpg','.jpeg','.gif','.zip' }
$found = 0
foreach ($f in $files) {
  $text = Get-Content -LiteralPath $f.FullName -Raw -ErrorAction SilentlyContinue
  if (-not $text) { continue }
  foreach ($k in $patterns.Keys) {
    foreach ($m in [regex]::Matches($text, $patterns[$k])) {
      $found++
      Write-Host ("[{0}] {1}: {2}" -f $k, $f.FullName.Substring($root.Path.Length + 1), $m.Value) -ForegroundColor Yellow
    }
  }
}
if ($found -eq 0) { Write-Host 'Scan clean: no findings.' -ForegroundColor Green; exit 0 }
Write-Host "$found finding(s). Review before publishing." -ForegroundColor Red; exit 1
