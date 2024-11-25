import typing as t


class Stat:

    def __init__(self) -> None:
        self.value = 0.0
        self.count = 0

    def __str__(self) -> str:
        return "Average"

    def add(self, value: float):
        self.value += value
        self.count += 1

    def get(self) -> t.Tuple[float, float, float]:
        if self.count == 0:
            return 0
        return self.value / self.count
