# Windows setup

Install Python 3.12, then run these commands in PowerShell
from the repository root.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe simulation.py
```

These commands use the virtual environment directly;
activating it is not required.

Run from the repository root so relative image paths resolve.
