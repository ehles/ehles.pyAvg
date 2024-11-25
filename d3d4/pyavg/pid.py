
class Stat:
    def __init__(self, alpha: float = 0.5, beta: float = 0.3, gamma: float = 0.2, integral_limit: float = 200):
        """
        Initialize Stats with PID-like smoothing parameters.
        :param alpha: Proportional coefficient.
        :param beta: Integral coefficient.
        :param gamma: Derivative coefficient.
        """

        # alpha + beta should ber equal 1 for better percision
        if not (0 < alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1):
            raise ValueError("alpha, beta, and gamma must be in the range [0, 1] and alpha > 0")

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.integral_limit = integral_limit

        self.value_integral = 0.0
        self.value_prev = None
        self.value_avg = 0.0

    def __str__(self) -> str:
        return f'PID <α:{self.alpha},β:{self.beta},γ:{self.gamma},δ:{self.integral_limit}>'

    def add(self, value: float):
        """
        Update hit statistics with a new duration.
        :param start: Start time in seconds.
        :param end: End time in seconds.
        """

        # Update integral component
        # self.value_integral += duration
        self.value_integral = (
            self.value_integral * (self.integral_limit - 1) + value
        ) / self.integral_limit

        # Update derivative component
        derivative = 0.0
        if self.value_prev is not None:
            derivative = value - self.value_prev

        # Calculate new average with PID components
        self.value_avg = (
            self.alpha * value +
            self.beta * self.value_integral +
            self.gamma * derivative
        )

        # Store current value for next derivative calculation
        self.value_prev = value

    def get(self) -> float:
        """
        Get the current average value.
        :return: Average value.
        """
        return self.value_avg
