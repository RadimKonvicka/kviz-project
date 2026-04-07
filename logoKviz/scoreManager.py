from dataclasses import dataclass


@dataclass
class ScoreManager:
    score: int = 0
    taskScore: int = 200
    revealCount: int = 0
    wrongPenalty: int = 20

    def costForReveal(self) -> int:
        # první odhalení zdarma, potom -2, -4, -8 ... (2^revealCount)
        if self.revealCount == 0:
            return 0
        return - (2 ** self.revealCount)

    def reveal(self):
        cost = self.costForReveal()
        self.taskScore += cost
        if self.taskScore < 0:
            self.taskScore = 0
        self.revealCount += 1
        return cost

    def penalizeWrong(self) -> int:
        self.taskScore -= self.wrongPenalty
        if self.taskScore < 0:
            self.taskScore = 0
        return -self.wrongPenalty

    def awardCorrect(self):
        self.score += self.taskScore
        self.taskScore = 200  # reset pro další úlohu
        self.revealCount = 0  # reset počtu odhalení
