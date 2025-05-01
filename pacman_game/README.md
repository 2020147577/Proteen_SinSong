# How to Run the Pac-Man Game

This guide walks you through setting up, installing, running, and testing the Pac-Man game on both macOS and Windows.

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.10+** installed and on your `PATH`  
- **pip** (Python’s package installer)  
- A **virtual environment** tool (built into Python)

---

## ⚙️ Setup & Installation

### 1. Create & activate a virtual environment

#### macOS / Linux
```bash
# from your project root (the folder containing setup.py)
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)
```powershell
# from your project root
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
> **Tip:** In Command Prompt (cmd.exe), use:
> ```bat
> .\.venv\Scripts\activate.bat
> ```

---

### 2. Upgrade pip

```bash
pip install --upgrade pip
```

---

### 3. Install the package in editable mode

```bash
pip install -e .
```

This does two things:

1. Installs your `pacman` package into the virtual environment  
2. Creates a console script `pacman` so you can launch the game simply by typing `pacman`

---

## ▶️ Running the Game

Once installed:
   ```bash
   python -m pacman
   ```
