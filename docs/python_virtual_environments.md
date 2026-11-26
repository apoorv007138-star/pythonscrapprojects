# Python virtual environments

A virtual environment keeps a project's installed packages separate from other Python projects.

## Create one

```bash
python -m venv .venv
```

## Activate it

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

## Install and record dependencies

```bash
python -m pip install requests
python -m pip freeze > requirements.txt
```

Install the recorded dependencies later with:

```bash
python -m pip install -r requirements.txt
```

When finished, run `deactivate` to leave the environment.
