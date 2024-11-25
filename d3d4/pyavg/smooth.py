import math
from time import monotonic_ns


class Stat:

    def __init__(self, tau=60):
        self.hit_rate = 0.0
        self.value_avg = 0.0
        self.miss_avg_duration = 0.0
        self.last_update = 0
        self.tau = tau
        self.total_hits = 0
        self.total_misses = 0

    def __str__(self) -> str:
        return f'Smooth <τ:{self.tau}>'

    def _update_smooth(self, old_value, current_value, elapsed_time):
        exp_factor = math.exp(-elapsed_time / self.tau)
        return old_value * exp_factor + current_value * (1 - exp_factor)

    def add(self, value: float):
        now = monotonic_ns()
        time_since_update = now - self.last_update

        # Update smoothed averages
        self.value_avg = self._update_smooth(self.value_avg, value, time_since_update)

        # Update last update timestamp
        self.last_update = now

    def get(self):
        return self.value_avg
