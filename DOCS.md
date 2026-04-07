# LogoKviz - Dokumentace

## 🎮 Co je to LogoKviz?
**LogoKviz** je jednoduchá kvízová hra v Pythonu s Pygame. Hráči hádají názvy log podle obrázků.

#### `Game` (logoKviz/game.py)
- Tohle řídí celou hru
- Spravuje aktuální kolo
- Spojuje všechny ostatní části

#### `TaskManager` (logoKviz/taskManager.py)
- Načítá a rozšifruje soubor s otázkami
- Používá XOR šifrování s klíčem, aby to nebylo úplně jednoduché
- Kontroluje, jestli soubory existují a tak

#### `AnswerChecker` (logoKviz/answerChecker.py)
- Kontroluje odpovědi pomocí SHA-256 hashe se saltem
- Chrání správné odpovědi před přímým čtením
- Salt dělá, že je to bezpečnější

#### `ScoreManager` (logoKviz/scoreManager.py)
- Počítá body a tresty
- Základní systém: 200 bodů za správně, -20 za špatně

#### `Timer` (logoKviz/timer.py)
- Jednoduchý časovač (výchozí 10 minut)
- Kontroluje, jestli čas nevypršel

#### `MinimalGameUI` (main.py)
- Grafické rozhraní s Pygame
- Minimalistický design v šedé a fialové
- Zobrazuje obrázky a spravuje vstup

### Nastavení (logoKviz/config.py)
- Všechny barvy, velikosti fontů a texty na jednom místě
- Snadno se mění vzhled bez úprav kódu
- Konstanty pro celou appku

## 🎨 Design a UI

### Barvy
- **Hlavní fialová**: `rgb(138, 43, 226)` - hlavní věci
- **Druhá fialová**: `rgb(186, 85, 211)` - akcenty
- **Světle šedá**: `rgb(245, 245, 245)` - pozadí
- **Tmavě šedá**: `rgb(60, 60, 60)` - text
- **Červená**: `rgb(220, 50, 50)` - chyby

### Minimalistický styl
- Čisté, jednoduché rozhraní
- Zaměřené na obsah (obrázky log)
- Bez zbytečných ozdob
- Přehledné písmo

## 🔒 Ochrana dat

### Šifrování
- Otázky a odpovědi jsou v šifrovaném JSON souboru (`data/tasks.json.enc`)
- Používá se jednoduché XOR s 16-bytovým klíčem (`data/key.bin`)
- Zabrání tomu, aby si někdo jednoduše přečetl data

### Hashování odpovědí
- Odpovědi jsou uložené jen jako salted SHA-256 hashe
- Každá má svůj salt pro větší bezpečnost
- Kontrola porovnává hashe, ne čte plaintext

### Co to neumí
- XOR není super bezpečné
- Klíč je v projektu (pro ukázku)
- Pro reálné použití by chtělo AES a správu klíčů

## 📊 Jak hra funguje

### Body
- **Základ**: 200 bodů za úlohu
- **Trest**: -20 bodů za špatně
- **Časový limit**: 10 minut celkem

### Průběh hry
1. **Menu**: Zobrazení náhodných log + tlačítko START
2. **Hra**: Zobrazení loga + instrukce "Jaké je to logo?"
3. **Vstup**: Hráč píše odpověď
4. **Vyhodnocení**: Kontrola správnosti + zobrazení výsledku
5. **Pokračování**: Další úloha nebo konec

## 🛠️ Technické věci

### Knihovny
- **Pygame**: Grafika a události
- **Pillow (PIL)**: Obrázky (načítání, velikost)

### Soubory
- `questions.json`: Zdrojové otázky (pro vývoj)
- `data/tasks.json.enc`: Šifrované úlohy (produkce)
- `data/key.bin`: Šifrovací klíč
- `img/*.png`: Obrázky log

### Chyby
- Chybí klíč nebo data → `FileNotFoundError`
- Špatné dekódování → `ValueError`
- Žádná úloha → `RuntimeError`

## 🚀 Spuštění

```bash
# S grafikou
python main.py

# Test bez GUI
python main.py --headless
```

## 📝 Poznámky k vývoji

Projekt jsem kompletně předělal:
- **Dřív**: starý balíček, snake_case, tradiční UI
- **Teď**: `logoKviz` balíček, camelCase, minimalistický design
- Zachoval jsem funkcionalitu, ale zlepšil design a kód
