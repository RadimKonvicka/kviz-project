# 🎮 LogoKviz - Minimalistická Kvízová Hra

Moderní kvízová hra s **minimalistickým designem** v barvách **šedé a fialové**. Elegantní, čistý interface se zaměřením na uživatelský komfort.

## Obsah

- Minimalistický design s přehledným přístupem
- Barvové schéma: šedá + fialová
- camelCase konvence pro všechny proměnné a soubory
- GUI s Pygame

## Struktura projektu

```
logoKviz-hra-konvicka/
├── main.py                 # Spouštěč aplikace
├── logoKviz/               # Balíček aplikace
│   ├── __init__.py
│   ├── config.py           # Konfigurační soubor
│   ├── game.py             # Game engine
│   ├── taskManager.py      # Správa úloh
│   ├── scoreManager.py     # Správa skóre
│   ├── timer.py            # Časovač
│   └── answerChecker.py    # Ověřování odpovědí
├── data/                   # Data
│   ├── tasks.json.enc      # Šifrované úlohy
│   └── key.bin             # Šifrovací klíč
├── img/                    # Obrázky
├── questions.json          # Zdrojové otázky
└── README.md               # Dokumentace
```

### Barvy
- **Primární fialová**: `rgb(138, 43, 226)`
- **Sekundární fialová**: `rgb(186, 85, 211)`
- **Světle šedá**: `rgb(245, 245, 245)`
- **Tmavě šedá**: `rgb(60, 60, 60)`
- **Mřížka**: `rgb(180, 180, 180)`

### Minimalistický přístup
- Jednoduché rozhraní
- Bez zbytečných prvků
- Fokus na obsah
- Elegantní typografie

## Spuštění

```bash
# Instalace závislostí
pip install -r requirements.txt

# Spuštění s GUI
python main.py

# Headless režim (test)
python main.py --headless
```

## 🎮 Jak hrát

**LogoKviz je hra, kde hádáš názvy log podle obrázků!**

1. **Stiskni SPACE** na úvodní obrazovce
2. **Podívej se na logo** v horní části obrazovky
3. **Napiš název loga** do vstupního pole (např. "python", "java", "cpp")
4. **ENTER** pro odeslání odpovědi
5. **SPACE** pro pokračování do další otázky
6. **ESC** pro návrat do menu

### Příklady otázek:
- Zobrazí se **Python logo** → správná odpověď: `python`
- Zobrazí se **C++ logo** → správná odpověď: `cpp`
- Zobrazí se **Java logo** → správná odpověď: `java`

## 🎯 Ovládání

- **SPACE** - Začít/Pokračovat
- **ENTER** - Odeslat odpověď
- **ESC** - Zpět do menu
- **Písmenka** - Psát odpověď
- **BACKSPACE** - Smazat znak



## Bezpečnost dat

Odpovědi jsou uloženy jako **salted SHA-256 hashe** v šifrovaném JSON souboru s jednoduchým XOR šifrováním. Tohle není bezpečné pro produkci - používejte AES pro skutečné aplikace.

---

**LogoKviz - Minimalistická a elegantní kvízová hra**
