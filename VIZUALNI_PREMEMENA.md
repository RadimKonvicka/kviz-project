# 🎨 LogoKviz - Průvodce Vizuální Transformací

## Co Se Změnilo?

Projekt byl kompletně přepracován na **"LogoKviz"** s novým minimalistickým designem.

---

## 📊 Souhrn Změn

### 🎨 Vizuální Transformace

| Aspekt | Dřív | Teď |
|--------|------|-----|
| **Název** | Původní | LogoKviz |
| **Barvy** | Výchozí | Šedá + Fialová |
| **Design** | Tradičnní puzzle | Minimalistický |
| **UI** | Mřížka a obrázky | Čistý interface |
| **Nálada** | Stresující | Minimalistická |

### 💻 Kódové Refaktorování

#### Jmenování Souborů
```
Dřív:              Teď:
answer_checker.py  → answerChecker.py
task_manager.py    → taskManager.py
score_manager.py   → scoreManager.py
```

#### Jmenování Proměnných
```python
# Dřív (snake_case)
self.base_path
self.task_manager
self.answer_buffer

# Teď (camelCase)
self.basePath
self.taskManager
self.userAnswer
```

#### Balíčky
```
původní/  →  logoKviz/
```

---

## 🎯 Nové Funkce

### 1. **Konfigurační Systém**
Nový `logoKviz/config.py` s centralizovaným nastavením:
- Barvy
- Velikosti fontů
- Textové zprávy
- Herní parametry

### 2. **Minimalistické UI**
- Šedá pozadí
- Fialové zvýraznění
- Elegantní typografie
- Bez zbytečných prvků

### 3. **Vylepšené Menu**
- Úvodní obrazovka s názvem
- Počet dostupných úloh
- Elegantní tlačítko START
- Čistý design

### 4. **Jednodušší Hrání**
- Přímý textový vstup
- Minimální informace
- Skóre a čas v přehledu
- Jasné výsledky

---

## 🔧 Technické Změny

### Imports
```python
from logoKviz.answerChecker import AnswerChecker
from logoKviz.game import Game
from logoKviz.config import *
```

### Metody
```python
# Dřív
self.game.start_round()
self.game.submit_answer()
self.game.reveal_piece()

# Teď
self.game.startRound()
self.game.submitAnswer()
self.game.revealPiece()
```

---

## 🎨 Barvy

### Primární Paleta
```
Fialová (Primary)      #8A2BE2 rgb(138, 43, 226)
Fialová Light          #BA55D3 rgb(186, 85, 211)
```

### Sekundární Paleta
```
Šedá Light (BG)        #F5F5F5 rgb(245, 245, 245)
Šedá Dark (Text)       #3C3C3C rgb(60, 60, 60)
Šedá Grid              #B4B4B4 rgb(180, 180, 180)
```

### Speciální
```
Chyba                  #DC3232 rgb(220, 50, 50)
Úspěch                 #50B450 rgb(80, 180, 80)
```

---

## 📱 UI Komponenty

### Menu Obrazovka
```
┌─────────────────────────────────┐
│                                 │
│         LogoKviz               │
│    Minimalistická kvízová hra   │
│                                 │
│      5 otázek čeká na tebe     │
│                                 │
│           [ START ]             │
│                                 │
│   Stiskni SPACE pro začátek    │
└─────────────────────────────────┘
```

### Hrací Obrazovka
```
┌─────────────────────────────────┐
│ Úloha 1/5                       │
│                                 │
│ Jaké je správné jméno?          │
│                                 │
│ Tvoje odpověď:                  │
│ ─────────────────────────────── │
│                                 │
│ Skóre: 200          Čas: 600s   │
│                                 │
│   ENTER: Odeslat | ESC: Zpět    │
└─────────────────────────────────┘
```

### Výsledková Obrazovka
```
┌─────────────────────────────────┐
│                                 │
│        ✓ Správně!              │
│                                 │
│        Skóre: 1200             │
│                                 │
│          [ DÁLE ]              │
│                                 │
│  SPACE: Další | ESC: Menu      │
└─────────────────────────────────┘
```

---

## 🚀 Spuštění

### S GUI (Nový Design)
```bash
python main.py
```

### Bez GUI (Test)
```bash
python main.py --headless
```

---

## 📂 Souborová Struktura

```
logoKviz-hra-konvicka/
├── main.py
├── README.md                    # Nová dokumentace
├── Instructions.md              # Tento soubor
├── logoKviz/                    # Nový balíček
│   ├── __init__.py
│   ├── config.py               # NOVÝ: Konfigurace
│   ├── game.py
│   ├── taskManager.py          # Přejmenovaný
│   ├── scoreManager.py         # Přejmenovaný
│   ├── timer.py
│   └── answerChecker.py        # Přejmenovaný
├── data/
│   ├── tasks.json.enc
│   └── key.bin
├── img/
└── questions.json
```

---

## ✨ Zajímavé Detaily

### Minimalistické Principy
1. **Bez zbytečných prvků** - Pouze Essential UI
2. **Jednostranné barvy** - Šedá + Fialová
3. **Čistá typografie** - Jasné písmo
4. **Prázdné místo** - Dýchá a relaxuje
5. **Jasná hierarchie** - Co je důležité?

### Kód je Čitelnější
- camelCase = snazší čtení
- Lepší pojmenování metod
- Centralizovaná konfigurace
- Konzistentní styl

---

## 🔮 Budoucí Možnosti

- [ ] Tmavý režim (Dark Mode)
- [ ]Animace přechodů
- [ ] Zvukové efekty
- [ ] Statistiky hráče
- [ ] Více témat barev
- [ ] Leaderboard

---

## 📝 Poznámky

> **Všechny funkce zůstaly zachovány** - Jedinou změnou je design, pojmenování a struktura kódu. Hra funguje stejně jako dřív, jen vypadá lépe! 🎨

---

**Projekt LogoKviz** - Minimalistická elegance v kvízové hře ✨
