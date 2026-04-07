# LogoKviz - Instrukce pro uživatele

## 🎮 Co je LogoKviz?

**LogoKviz** je zábavná kvízová hra, kde hádáš názvy log podle obrázků. Hra má minimalistický design v šedé a fialové a je napsaná v Pythonu s Pygame.

## 🎯 Cíl hry

Hráč se učí poznávat loga různých technologií, jazyků a platforem. Správně uhodneš = body, špatně = penalizace. Hra je časově omezená.

## 📋 Herní pravidla

### Bodování
- **Správná odpověď**: +200 bodů
- **Špatná odpověď**: -20 bodů
- **Časový limit**: 10 minut celkem

### Průběh hry
1. **Úvodní obrazovka**: Zobrazí se několik log a tlačítko START
2. **Herní kolo**: Zobrazí se jeden velký obrázek loga
3. **Otázka**: "Jaké je to logo?"
4. **Odpověď**: Napiš název loga (např. "python", "java", "cpp")
5. **Vyhodnocení**: Zobrazí se výsledek (✓ Správně / ✗ Špatně)
6. **Pokračování**: Další logo nebo konec hry

## 🎮 Ovládání

### Klávesy
- **SPACE**: Začít hru / Pokračovat do další otázky
- **ENTER**: Odeslat odpověď
- **ESC**: Zpět do menu
- **Písmenka**: Psát odpověď
- **BACKSPACE**: Smazat znak

### Příklady odpovědí
- Python logo → `python`
- C++ logo → `cpp`
- Java logo → `java`
- Linux logo → `linux`
- Windows logo → `windows`

## 🎨 Uživatelské rozhraní

### Menu
- Zobrazuje 3 náhodné loga pro ukázku
- Velký nadpis "LogoKviz"
- Popis "Minimalistická kvízová hra"
- Tlačítko START

### Herní obrazovka
- **Velký obrázek loga** (200x200 pixelů) v horní části
- **Instrukce**: "Jaké je to logo?"
- **Číslo úlohy**: "Úloha 1/5"
- **Vstupní pole**: Pro napsání odpovědi
- **Skóre**: Aktuální počet bodů
- **Čas**: Zbývající čas v sekundách

### Výsledková obrazovka
- **Obrázek loga** v horní části
- **Výsledek**: ✓ Správně nebo ✗ Špatně
- **Skóre**: Aktuální počet bodů
- **Tlačítko**: "DÁLE" pro pokračování

## 🛠️ Technické požadavky

### Systémové požadavky
- **Operační systém**: Windows, macOS nebo Linux
- **Python**: Verze 3.7 nebo vyšší
- **Paměť**: Minimálně 100 MB volné RAM
- **Grafika**: Jakákoliv grafická karta podporující OpenGL

### Instalace
```bash
# Naklonování projektu
git clone <repository-url>
cd logoKviz-hra-konvicka

# Vytvoření virtuálního prostředí
python -m venv .venv

# Aktivace prostředí
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Instalace závislostí
pip install -r requirements.txt
```

### Spuštění
```bash
# Grafický režim (doporučeno)
python main.py

# Test režim (bez GUI)
python main.py --headless
```

## 📁 Struktura projektu

```
logoKviz-hra-konvicka/
├── main.py                    # Hlavní spouštěč
├── logoKviz/                  # Balíček aplikace
│   ├── __init__.py
│   ├── config.py             # Konfigurace (barvy, texty)
│   ├── game.py               # Herní logika
│   ├── taskManager.py        # Správa otázek
│   ├── scoreManager.py       # Bodování
│   ├── timer.py              # Časovač
│   └── answerChecker.py      # Kontrola odpovědí
├── data/                     # Šifrovaná data
│   ├── tasks.json.enc        # Otázky a odpovědi
│   └── key.bin               # Šifrovací klíč
├── img/                      # Obrázky log
│   ├── cpp_logo.png
│   ├── java_logo.png
│   ├── python_logo.png
│   ├── windows.png
│   └── linux.jpg
├── questions.json            # Zdrojové otázky
├── README.md                 # Dokumentace
├── DOCS.md                   # Technická dokumentace
└── Instructions.md           # Tyto instrukce
```

## 🔒 Bezpečnost dat

Odpovědi jsou chráněny pomocí:
- **SHA-256 hashování** se saltem
- **XOR šifrování** datového souboru
- Odpovědi nejsou uloženy v čitelné podobě

## 🆘 Řešení problémů

### Hra se nespustí
```bash
# Zkontrolujte instalaci závislostí
pip install pygame pillow

# Zkontrolujte Python verzi
python --version
```

### Chybí obrázky
- Ujistěte se, že složka `img/` obsahuje všechny potřebné soubory
- Obrázky musí být ve formátu PNG nebo JPG

### Špatné odpovědi
- Odpovědi jsou case-insensitive (malá/velká písmena)
- Diakritika se ignoruje
- Mezery se odstraňují

## 📞 Kontakt

Pro dotazy nebo problémy kontaktujte autora projektu.

---

**LogoKviz - Minimalistická elegance v kvízové hře!** 🎨✨

## Doporučené rozšíření
Student může přidat: více úrovní obtížnosti, různé typy úloh, například osobnost, logo, hardware, programovací jazyk, zvukový doprovod, animované odhalování, žebříček týmů, režim pro správce soutěže, ve kterém lze vybírat další úkol bez odhalení správného řešení soutěžícím.

## Doporučené třídy
ImagePuzzle, HintSystem, AnswerChecker, ScoreManager, Timer, RoundScreen, AdminPanel.
