@echo off
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0gryvids.ps1" %*
exit /b %ERRORLEVEL%
