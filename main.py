import argparse
import json
import random
import secrets
import sys
from pathlib import Path

from logoKviz.answerChecker import AnswerChecker
from logoKviz.game import Game
from logoKviz.config import *


class GamePackage:
    def __init__(self, basePath: Path):
        self.basePath = basePath
        self.storage = self.basePath / "data"
        self.payload = self.storage / "tasks.json.enc"
        self.secretKey = self.storage / "key.bin"
        self.questionsFile = self.basePath.parent / "questions.json"

    def prepare(self) -> None:
        if self.payload.exists():
            return
        self.storage.mkdir(parents=True, exist_ok=True)
        self._createPayload()

    def _createPayload(self) -> None:
        keyBytes = secrets.token_bytes(16)
        self.secretKey.write_bytes(keyBytes)

        with self.questionsFile.open("r", encoding="utf-8") as stream:
            questions = json.load(stream)

        taskList = []
        for itemId, entry in enumerate(questions, start=1):
            salt = secrets.token_hex(8)
            taskList.append(
                {
                    "id": itemId,
                    "title": entry["title"],
                    "image": entry["image"],
                    "salt": salt,
                    "hash": AnswerChecker.hashAnswer(entry["answer"], salt),
                }
            )

        rawBytes = json.dumps(taskList, ensure_ascii=False).encode("utf-8")
        encoded = bytes(value ^ keyBytes[index % len(keyBytes)] for index, value in enumerate(rawBytes))
        self.payload.write_bytes(encoded)


class HeadlessRun:
    def __init__(self, rootPath: Path):
        self.rootPath = rootPath
        self.package = GamePackage(rootPath)
        self.game = Game(str(self.rootPath / "data" / "tasks.json.enc"), str(self.rootPath / "data" / "key.bin"), timeLimit=60)

    def execute(self) -> None:
        self.package.prepare()
        self.game.load()
        self.game.startRound(1)

        print("✓ Načteno úloh:", len(self.game.taskManager.tasks))
        print("✓ Název:", self.game.currentTask["title"])

        for answer in ["python", "java"]:
            result = self.game.submitAnswer(answer)
            print(f"Odpověď '{answer}' ->", result, "Skóre:", self.game.scoreManager.score)


class MinimalGameUI:
    def __init__(self, rootPath: Path):
        self.rootPath = rootPath
        self.package = GamePackage(rootPath)
        self.package.prepare()
        self.game = Game(str(rootPath / "data" / "tasks.json.enc"), str(rootPath / "data" / "key.bin"), timeLimit=DEFAULT_TIME_LIMIT)
        self.game.load()
        
        # Použití konfigurace
        self.COLOR_BG = COLOR_BG
        self.COLOR_TEXT_DARK = COLOR_TEXT_DARK
        self.COLOR_PRIMARY = COLOR_PRIMARY
        self.COLOR_SECONDARY = COLOR_SECONDARY
        self.COLOR_GRID = COLOR_GRID
        self.COLOR_ERROR = COLOR_ERROR
        self.COLOR_SUCCESS = COLOR_SUCCESS
        
        self.screenWidth = WINDOW_WIDTH
        self.screenHeight = WINDOW_HEIGHT
        self.font = None
        self.screen = None
        self.clock = None
        self.currentIndex = 0
        self.tasks = []
        self.userAnswer = ""
        self.gameState = "menu"  # menu, playing, result
        self.lastResult = None
        self.logoImages = {}  # Cachované obrázky
        self.currentTaskImage = None

    def _loadTasks(self) -> None:
        self.tasks = list(self.game.taskManager.tasks)
        random.shuffle(self.tasks)

    def _initPygame(self):
        import pygame
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption(f"{TEXT_LOGO} - {TEXT_SUBTITLE}")
        self.fontLarge = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.fontMedium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.fontSmall = pygame.font.Font(None, FONT_SIZE_SMALL)
        self.fontTiny = pygame.font.Font(None, FONT_SIZE_TINY)
        self.clock = pygame.time.Clock()
        self._loadImages()

    def _loadImages(self):
        from PIL import Image
        import pygame
        
        imgDir = self.rootPath / "img"
        images = ["cpp_logo.png", "java_logo.png", "python_logo.png", "windows.png", "linux.jpg"]
        
        for imgFile in images:
            imgPath = imgDir / imgFile
            if imgPath.exists():
                try:
                    img = Image.open(imgPath)
                    img = img.convert("RGBA")
                    img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Větší obrázek pro hru
                    pygameSurf = pygame.image.frombytes(img.tobytes(), img.size, img.mode)
                    keyName = Path(imgFile).stem
                    self.logoImages[keyName] = pygameSurf
                except Exception as e:
                    print(f"Chyba při načítání {imgFile}: {e}")

    def _drawMenu(self):
        import pygame
        
        self.screen.fill(self.COLOR_BG)
        
        # Zobrazit náhodné loga nahoru
        logosToShow = list(self.logoImages.values())[:3]
        if logosToShow:
            xStart = (self.screenWidth - (len(logosToShow) * 120)) // 2
            for i, logo in enumerate(logosToShow):
                x = xStart + i * 120
                self.screen.blit(logo, (x, 20))
        
        # Hlavní titul
        titleText = self.fontLarge.render(TEXT_LOGO, True, self.COLOR_PRIMARY)
        self.screen.blit(titleText, (self.screenWidth // 2 - titleText.get_width() // 2, 140))
        
        # Podtitul
        subtitleText = self.fontSmall.render(TEXT_SUBTITLE, True, self.COLOR_TEXT_DARK)
        self.screen.blit(subtitleText, (self.screenWidth // 2 - subtitleText.get_width() // 2, 220))
        
        # Popis
        descText = self.fontTiny.render(f"{len(self.tasks)} otázek čeká na tebe", True, self.COLOR_GRID)
        self.screen.blit(descText, (self.screenWidth // 2 - descText.get_width() // 2, 250))
        
        # Tlačítko Start
        startBtn = pygame.Rect(self.screenWidth // 2 - 100, 400, 200, 60)
        pygame.draw.rect(self.screen, self.COLOR_PRIMARY, startBtn)
        pygame.draw.rect(self.screen, self.COLOR_SECONDARY, startBtn, BUTTON_BORDER)
        startText = self.fontMedium.render(MSG_BUTTON_START, True, self.COLOR_BG)
        self.screen.blit(startText, (startBtn.x + startBtn.width // 2 - startText.get_width() // 2, 
                                      startBtn.y + startBtn.height // 2 - startText.get_height() // 2))
        
        # Instrukce
        hintText = self.fontTiny.render(MSG_START, True, self.COLOR_SECONDARY)
        self.screen.blit(hintText, (self.screenWidth // 2 - hintText.get_width() // 2, 600))

    def _drawPlaying(self):
        import pygame
        
        self.screen.fill(self.COLOR_BG)
        
        if self.currentIndex >= len(self.tasks):
            self.gameState = "menu"
            return
        
        task = self.tasks[self.currentIndex]
        
        # Zobrazit logo aktuální úlohy větší
        imagePath = task.get("image", "")
        if imagePath:
            imgName = Path(imagePath).stem
            if imgName in self.logoImages:
                logo = self.logoImages[imgName]
                self.screen.blit(logo, (self.screenWidth // 2 - 100, 50))  # Větší a uprostřed
        
        # Číslo úlohy
        taskNumText = self.fontSmall.render(f"{TEXT_TASK} {self.currentIndex + 1}/{len(self.tasks)}", True, self.COLOR_SECONDARY)
        self.screen.blit(taskNumText, (50, 280))
        
        # Instrukce místo otázky
        instructionText = self.fontMedium.render("Jaké je to logo?", True, self.COLOR_TEXT_DARK)
        self.screen.blit(instructionText, (self.screenWidth // 2 - instructionText.get_width() // 2, 280))
        
        # Vstupní pole
        pygame.draw.line(self.screen, self.COLOR_PRIMARY, (50, 350), (850, 350), INPUT_BORDER)
        answerText = self.fontSmall.render(self.userAnswer, True, self.COLOR_PRIMARY)
        self.screen.blit(answerText, (60, 360))
        
        # Skóre
        scoreText = self.fontSmall.render(f"{TEXT_SCORE} {self.game.scoreManager.score}", True, self.COLOR_PRIMARY)
        self.screen.blit(scoreText, (50, 430))
        
        # Časový limit
        remainingTime = self.game.timer.remaining()
        timeColor = self.COLOR_ERROR if remainingTime < 60 else self.COLOR_SECONDARY
        timeText = self.fontSmall.render(f"{TEXT_TIME} {remainingTime}s", True, timeColor)
        self.screen.blit(timeText, (50, 480))
        
        # Nápověda
        hintText = self.fontTiny.render(MSG_INPUT_HINT, True, self.COLOR_GRID)
        self.screen.blit(hintText, (50, 650))

    def _drawResult(self):
        import pygame
        
        self.screen.fill(self.COLOR_BG)
        
        # Zobrazit logo aktuální úlohy
        task = self.tasks[self.currentIndex] if self.currentIndex < len(self.tasks) else None
        if task:
            imagePath = task.get("image", "")
            if imagePath:
                imgName = Path(imagePath).stem
                if imgName in self.logoImages:
                    logo = self.logoImages[imgName]
                    self.screen.blit(logo, (self.screenWidth // 2 - 50, 50))
        
        # Výsledek
        if self.lastResult:
            resultText = self.fontLarge.render(MSG_CORRECT, True, self.COLOR_PRIMARY)
        else:
            resultText = self.fontLarge.render(MSG_WRONG, True, self.COLOR_ERROR)
        
        self.screen.blit(resultText, (self.screenWidth // 2 - resultText.get_width() // 2, 180))
        
        # Skóre
        scoreText = self.fontMedium.render(f"{TEXT_SCORE} {self.game.scoreManager.score}", True, self.COLOR_TEXT_DARK)
        self.screen.blit(scoreText, (self.screenWidth // 2 - scoreText.get_width() // 2, 300))
        
        # Pokračovací tlačítko
        continueBtn = pygame.Rect(self.screenWidth // 2 - 80, 420, 160, 50)
        pygame.draw.rect(self.screen, self.COLOR_SECONDARY, continueBtn)
        pygame.draw.rect(self.screen, self.COLOR_PRIMARY, continueBtn, BUTTON_BORDER)
        continueText = self.fontSmall.render(MSG_BUTTON_NEXT, True, self.COLOR_TEXT_DARK)
        self.screen.blit(continueText, (continueBtn.x + continueBtn.width // 2 - continueText.get_width() // 2,
                                         continueBtn.y + continueBtn.height // 2 - continueText.get_height() // 2))
        
        # Info
        infoText = self.fontTiny.render(MSG_CONTINUE_HINT, True, self.COLOR_GRID)
        self.screen.blit(infoText, (self.screenWidth // 2 - infoText.get_width() // 2, 650))

    def run(self) -> None:
        import pygame
        
        self._initPygame()
        self._loadTasks()
        
        running = True
        while running:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.gameState == "menu":
                        if event.key == pygame.K_SPACE:
                            self.gameState = "playing"
                            self.currentIndex = 0
                            self.userAnswer = ""
                    elif self.gameState == "playing":
                        if event.key == pygame.K_BACKSPACE:
                            self.userAnswer = self.userAnswer[:-1]
                        elif event.key == pygame.K_RETURN:
                            if self.currentIndex < len(self.tasks):
                                task = self.tasks[self.currentIndex]
                                self.game.startRound(task["id"])
                                self.lastResult = self.game.submitAnswer(self.userAnswer)
                                self.gameState = "result"
                        elif event.key == pygame.K_ESCAPE:
                            self.gameState = "menu"
                            self.userAnswer = ""
                        elif event.unicode.isprintable():
                            if len(self.userAnswer) < 100:
                                self.userAnswer += event.unicode
                    elif self.gameState == "result":
                        if event.key == pygame.K_SPACE:
                            self.currentIndex += 1
                            self.userAnswer = ""
                            if self.currentIndex >= len(self.tasks):
                                self.gameState = "menu"
                            else:
                                self.gameState = "playing"
                        elif event.key == pygame.K_ESCAPE:
                            self.gameState = "menu"
                            self.userAnswer = ""
            
            # Vykreslování
            if self.gameState == "menu":
                self._drawMenu()
            elif self.gameState == "playing":
                self._drawPlaying()
            elif self.gameState == "result":
                self._drawResult()
            
            pygame.display.flip()
        
        pygame.quit()




def main() -> None:
    parser = argparse.ArgumentParser(description="LogoKviz - Minimalistická kvízová hra")
    parser.add_argument("--headless", action="store_true", help="Spustit bez GUI (test)")
    options = parser.parse_args()
    basePath = Path(__file__).resolve().parent

    if options.headless:
        HeadlessRun(basePath).execute()
    else:
        MinimalGameUI(basePath).run()


if __name__ == "__main__":
    main()
