import time


class Timer:
    def __init__(self, seconds: int):
        self.total = seconds
        self.startTs = None

    def start(self):
        self.startTs = time.time()

    def remaining(self) -> int:
        if self.startTs is None:
            return self.total
        rem = int(self.total - (time.time() - self.startTs))
        return max(0, rem)

    def expired(self) -> bool:
        return self.remaining() <= 0
