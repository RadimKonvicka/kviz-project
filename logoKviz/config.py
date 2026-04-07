"""
Konfigurační soubor LogoKviz s minimalistickým designem.
Barvy: šedá a fialová
"""

# Barvy - minimalistická paleta
COLOR_PRIMARY = (138, 43, 226)  # Fialová - hlavní barva
COLOR_SECONDARY = (186, 85, 211)  # Světle fialová - sekundární
COLOR_BG = (245, 245, 245)  # Světle šedá - pozadí
COLOR_BG_DARK = (235, 235, 235)  # Tmavě šedá - sekundární pozadí
COLOR_TEXT_DARK = (60, 60, 60)  # Tmavě šedá - text
COLOR_TEXT_LIGHT = (200, 200, 200)  # Světle šedá - slabý text
COLOR_GRID = (180, 180, 180)  # Střední šedá - mřížka
COLOR_ERROR = (220, 50, 50)  # Červená - chyby
COLOR_SUCCESS = (80, 180, 80)  # Zelená - úspěch

# Rozměry okna
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

# Rozměry textu
FONT_SIZE_LARGE = 56
FONT_SIZE_MEDIUM = 40
FONT_SIZE_SMALL = 28
FONT_SIZE_TINY = 20

# Animace a přechody
ANIMATION_SPEED = 60  # FPS
BUTTON_PADDING = 20
BUTTON_BORDER = 3
INPUT_BORDER = 3

# Herní nastavení
DEFAULT_TIME_LIMIT = 600  # sekund
BASE_TASK_SCORE = 200
WRONG_PENALTY = 20

# Zprávy
MSG_START = "Stiskni SPACE pro začátek"
MSG_INPUT_HINT = "ENTER: Odeslat | ESC: Zpět"
MSG_CONTINUE_HINT = "SPACE: Další | ESC: Menu"
MSG_CORRECT = "✓ Správně!"
MSG_WRONG = "✗ Špatně"
MSG_BUTTON_START = "START"
MSG_BUTTON_NEXT = "DÁLE"
MSG_PAUSE = "PAUZA"

# UI Texty
TEXT_LOGO = "LogoKviz"
TEXT_SUBTITLE = "Minimalistická kvízová hra"
TEXT_SCORE = "Skóre:"
TEXT_TIME = "Čas:"
TEXT_TASK = "Úloha"

# Soubory a cesty
DATA_DIR = "data"
TASKS_FILE = "tasks.json.enc"
KEY_FILE = "key.bin"
QUESTIONS_FILE = "questions.json"
