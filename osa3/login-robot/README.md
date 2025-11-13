# login-robot

This folder contains a small command-line Python application and Robot Framework tests.

Quick start (Windows PowerShell)

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run Robot Framework tests

```powershell
# from the login-robot folder
.\.venv\Scripts\robot.exe src\tests
```

4. Test outputs

- Results are written to `results/output.xml`, `results/log.html`, and `results/report.html`.

Notes

- `AppLibrary.py` provides keywords that capture stdin/stdout for the application under test. Tests call `Run Application` to execute the program with prepared inputs.
- If you see strange failures, run a single test to speed up debugging:

```powershell
.\.venv\Scripts\robot.exe -t "Register With Valid Username And Password" src\tests\register.robot
```
