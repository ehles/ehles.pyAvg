import typing as t


class Stat:

    def __init__(self, alpha: float) -> None:
        self.hit_avg = 0.0
        self.average = 0.0
        self.duration_miss = 0.0

        self.alpha = 1
        self.steps = 1
        if alpha > 1:
            self.steps = alpha
            self.is_avg = True
        elif alpha <= 1:
            self.alpha = alpha
            self.is_avg = False

    def __str__(self) -> str:
        return f"ExpSmooth <α:({self.alpha},s:{self.steps})>"

    def simgle_average(self, value: float):
        return (self.average * (self.steps - 1) + value) / self.steps

    def exponential_average(self, value: float):
        return (self.alpha * value + (1 - self.alpha) * self.average)

    def add(self, value: float):
        if self.is_avg:
            self.average = self.simgle_average(value)
        else:
            self.average = self.exponential_average(value)

    def get(self) -> t.Tuple[float, float, float]:
        return self.average
