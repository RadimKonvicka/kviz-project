import hashlib


class AnswerChecker:
    """Kontroluje odpovědi srovnáním se uloženými soltenými SHA-256 hashy."""

    @staticmethod
    def _normalize(text: str) -> str:
        return "".join(text.strip().lower().split())

    @staticmethod
    def hashAnswer(answer: str, salt: str) -> str:
        norm = AnswerChecker._normalize(answer)
        h = hashlib.sha256()
        h.update(salt.encode("utf-8"))
        h.update(norm.encode("utf-8"))
        return h.hexdigest()

    def check(self, answer: str, salt: str, expectedHash: str) -> bool:
        return self.hashAnswer(answer, salt) == expectedHash
