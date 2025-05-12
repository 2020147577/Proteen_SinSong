# 🟡 Pac-Man 게임 실행 방법 (Mac & Windows)

---

## ⚙️ Python 설치 및 환경 준비

### 1. Python 설치 (버전 3.12 기준)

#### macOS

```bash
brew install python
```

#### Windows (PowerShell)

```powershell
winget install --id Python.Python.3.12
```

### 설치 확인

```bash
python --version
```

→ `Python 3.12.x`가 출력되어야 합니다.

---

## ⚙️ 가상 환경 설정 및 설치

### 2. 가상 환경 생성 및 활성화

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **명령 프롬프트(cmd.exe)** 를 사용하는 경우:
>
> ```bat
> .\.venv\Scripts\activate.bat
> ```

---

### 3. pip 업그레이드

```bash
pip install --upgrade pip
```

---

### 4. 패키지 설치 (requirements.txt)

```bash
pip install -r requirements.txt
```

→ Pac-Man 게임이 동작하는 데 필요한 외부 라이브러리들을 설치합니다.

---

### 5. 개발(editable) 모드로 패키지 설치

```bash
pip install -e .
```

→ 로컬 개발 버전을 가상환경에 등록하여, `pacman` 명령어로 바로 실행 가능하게 만듭니다.

---

## ▶️ 게임 실행 및 종료

### 🟢 실행:

```bash
python -m pacman
```

또는

```bash
pacman
```

### 🛑 종료:

1. 게임 창의 X 버튼 클릭
2. Ctrl + C (macOS, Windows 터미널 공통)

---

## ✅ 최종 실행 순서 요약 (Windows 기준 예시)

```powershell
winget install --id Python.Python.3.12
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
pacman
```
