import json
import os
from typing import List, Dict, Any


class TaskManager:
    """Načítá úlohy z kódovaného JSON souboru."""

    def __init__(self, dataPath: str, keyPath: str):
        self.dataPath = dataPath
        self.keyPath = keyPath
        self.tasks: List[Dict[str, Any]] = []

    def _loadKey(self) -> bytes:
        if not os.path.exists(self.keyPath):
            raise FileNotFoundError(f"Soubor s klíčem nenalezen: {self.keyPath}")
        with open(self.keyPath, "rb") as f:
            return f.read()

    def _decode(self, data: bytes, key: bytes) -> bytes:
        out = bytearray()
        keyLen = len(key)
        for i, b in enumerate(data):
            out.append(b ^ key[i % keyLen])
        return bytes(out)

    def loadTasks(self):
        if not os.path.exists(self.dataPath):
            raise FileNotFoundError(f"Datový soubor nenalezen: {self.dataPath}")
        key = self._loadKey()
        with open(self.dataPath, "rb") as f:
            enc = f.read()
        try:
            dec = self._decode(enc, key)
            data = json.loads(dec.decode("utf-8"))
        except Exception as e:
            raise ValueError(f"Chyba při dekódování: {e}")

        if not isinstance(data, list):
            raise ValueError("Soubor by měl obsahovat JSON seznam úloh")
        self.tasks = data

    def getTask(self, taskId: int) -> Dict[str, Any]:
        for t in self.tasks:
            if t.get("id") == taskId:
                return t
        raise KeyError(f"Úloha s ID {taskId} nenalezena")
