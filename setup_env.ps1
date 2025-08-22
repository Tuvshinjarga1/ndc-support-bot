# Microsoft Bot Framework Environment Variables Setup
# Энэ скриптийг PowerShell-д ажиллуулна

Write-Host "=== Microsoft Bot Framework Environment Setup ===" -ForegroundColor Green

# Environment variable-уудыг тохируулах
$env:MICROSOFT_APP_ID = "your_bot_app_id_here"
$env:MICROSOFT_APP_PASSWORD = "your_bot_app_password_here"
$env:MICROSOFT_APP_TENANT_ID = "your_tenant_id_here"

Write-Host "Environment variables set:" -ForegroundColor Yellow
Write-Host "MICROSOFT_APP_ID: $env:MICROSOFT_APP_ID" -ForegroundColor Cyan
Write-Host "MICROSOFT_APP_PASSWORD: $($env:MICROSOFT_APP_PASSWORD ? 'SET' : 'NOT SET')" -ForegroundColor Cyan
Write-Host "MICROSOFT_APP_TENANT_ID: $env:MICROSOFT_APP_TENANT_ID" -ForegroundColor Cyan

Write-Host "`nЭдгээр утгуудыг таны Microsoft Bot Framework App Registration-оос авна:" -ForegroundColor Yellow
Write-Host "1. Azure Portal -> App registrations -> Таны app -> Overview -> Application (client) ID" -ForegroundColor White
Write-Host "2. Azure Portal -> App registrations -> Таны app -> Certificates & secrets -> Client secrets" -ForegroundColor White
Write-Host "3. Azure Portal -> App registrations -> Таны app -> Overview -> Directory (tenant) ID" -ForegroundColor White

Write-Host "`nДараа нь python debug_env.py ажиллуулж тохиргоог шалгана уу." -ForegroundColor Green
