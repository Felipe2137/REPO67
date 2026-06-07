# REPO67

Minimalna aplikacja Python z prostym CLI i logiką „tiny fizzbuzz”.

## Quick Start

### 1. Klonowanie repozytorium

```bash
git clone <https://github.com/Felipe2137/REPO67>
cd REPO67

### 2. Stworzenie venv i instalacja zależności
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 3. Uruchamianie aplikacji
python single_app.py 

### 4. Linting i formatowanie 
bash scripts/format_code.sh #Formatowanie
bash scripts/format_check.sh #Sprawdzenie formatowania
bash scripts/lint.sh #Lintowanie
bash scripts/run_tests.sh #Testy

### 5. Continuous Integration (CI)

#Projekt używa GitHub Actions:

#Workflow znajduje się w .github/workflows/ci.yml.
#Pipeline uruchamia się automatycznie przy pushach i pull requestach na branże: main, develop.
#Pipeline wykonuje kolejno:
#Tworzy i aktywuje środowisko .venv.
#Instaluje zależności z requirements.txt.
#Sprawdza formatowanie kodu (black).
#Analizuje kod pod kątem błędów i stylu (pylint).
#Uruchamia testy jednostkowe (pytest).