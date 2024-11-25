from threading import Lock


class Stat:

    def __init__(self, alpha: float = 0.3, beta: float = 0.2):
        """
        Initialize Stats with smoothing parameters.

        :param alpha: Smoothing factor for average values.
        :param beta: Smoothing factor for trend values.
        """
        if not (0 < alpha <= 1 and 0 < beta <= 1):
            raise ValueError("alpha and beta must be in the range (0, 1]")

        self.alpha = alpha
        self.beta = beta

        self.avg = 0.0
        self.trend = 0.0

        self.lock = Lock()

    def __str__(self) -> str:
        return f"BiAvg <α:{self.alpha}, β:{self.beta}>"

    def add(self, value: float):
        """
        Update count statistics with a new duration.
        """
        with self.lock:
            prev_avg = self.avg
            self.avg = (self.alpha * value + (1 - self.alpha) *
                        (self.avg + self.trend))
            self.trend = (self.beta * (self.avg - prev_avg) +
                          (1 - self.beta) * self.trend)

    def get(self) -> float:
        """
        Get the current average count.
        :return: Average count.
        """
        return self.avg
