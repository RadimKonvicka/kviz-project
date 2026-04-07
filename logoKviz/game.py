from .taskManager import TaskManager
from .answerChecker import AnswerChecker
from .scoreManager import ScoreManager
from .timer import Timer


class Game:
    def __init__(self, dataPath: str, keyPath: str, timeLimit: int = 600):
        self.taskManager = TaskManager(dataPath, keyPath)
        self.answerChecker = AnswerChecker()
        self.scoreManager = ScoreManager()
        self.timer = Timer(timeLimit)
        self.currentTask = None

    def load(self):
        self.taskManager.loadTasks()

    def startRound(self, taskId: int):
        self.currentTask = self.taskManager.getTask(taskId)
        self.timer.start()

    def revealPiece(self):
        cost = self.scoreManager.reveal()
        return cost

    def submitAnswer(self, answer: str) -> bool:
        if self.currentTask is None:
            raise RuntimeError("Není aktivní úloha")
        ok = self.answerChecker.check(answer, self.currentTask["salt"], self.currentTask["hash"]) 
        if ok:
            self.scoreManager.awardCorrect()
        else:
            self.scoreManager.penalizeWrong()
        return ok
