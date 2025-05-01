# Pac-Man 게임 실행 방법

---

## 📋 사전 조건

- **Python 3.10 이상**이 설치되어 있고 `PATH`에 등록되어 있어야 합니다.  
- **pip** (파이썬 패키지 관리자)  
- **가상 환경** 도구 (파이썬 내장)

---

## ⚙️ 설정 및 설치

### 1. 가상 환경 생성 및 활성화

#### macOS / Linux
```bash
# project root(설치 스크립트가 있는 폴더)에서 실행
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)
```powershell
# project root에서 실행
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
> **팁:**  
> 명령 프롬프트(cmd.exe)를 사용 중이라면:
> ```bat
> .\.venv\Scripts\activate.bat
> ```

---

### 2. pip 업그레이드

```bash
pip install --upgrade pip
```

---

### 3. 개발(editable) 모드로 패키지 설치

```bash
pip install -e .
```

이 명령은 다음 두 가지를 수행:

1. 가상 환경에 `pacman` 패키지를 설치.  
2. `pacman` 콘솔 스크립트를 생성하여, 터미널에서 `pacman` 만 입력해도 게임을 실행할 수 있게 함.

---

## ▶️ 게임 실행 및 종료

### 🟢 실행:

설치가 완료된 후에는 아래 중 한 가지 방법으로 실행:

```bash
python -m pacman
```

또는

```bash
pacman
```

### 🛑 종료

게임 종료는 다음 두 가지 방법 중 하나로 할 수 있습니다:

1. **게임 창** 상단의 **X** 버튼 클릭  
2. **터미널**에서 **Ctrl + C** 입력 (macOS)
3. **PowerShell / 명령 프롬프트**에서 **Ctrl + C** 입력 (Windows)
