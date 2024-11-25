#!/usr/bin/env python

import random as r

import matplotlib.pyplot as plt

from d3d4.pyavg import bi_avg
from d3d4.pyavg import cumulative
from d3d4.pyavg import exp_smooth
from d3d4.pyavg import pid
from d3d4.pyavg import ring_buff
from d3d4.pyavg import smooth


class StatStub:
    """Just for referense actual values"""

    def __init__(self) -> None:
        self.value = 0.0

    def __str__(self) -> str:
        return "Value"

    def add(self, value: float):
        self.value = value

    def get(self) -> float:
        return self.value


def process(stats, events_count: int, interval: int):
    targets = [
        [0, 5, 0.9],
        [10, 20, 0.6],
        [20, 25, 0.3],
        [25, 40, 0.6],
        [40, 41, 0.7],
        [41, 60, 0.6],
        [60, 61, 0.2],
        [61, 64, 0.6],
        [64, 66, 0.7],
        [66, 67, 0.75],
        [67, 95, 0.6],
        [95, 100, 1],
    ]
    disp = 100
    base = 3000
    value = 0
    for i in range(events_count):
        d = r.randint(-disp, disp)
        value = base + d

        p = i / events_count * 100
        for trgt in targets:
            if trgt[0] < p <= trgt[1]:
                m = trgt[2]
                value = base * m + d
                break
        for s in stats:
            s.add(value)

        if i % interval == 0:
            yield {
                'avg': {str(s): s.get() for s in stats},
            }


def main():
    iterations = 100_000
    get_interval = 100
    stats = [
        StatStub(),
        cumulative.Stat(),
        ring_buff.Stat(100),
        bi_avg.Stat(0.02, 0.1),

        # # # for 1m events
        # # exp_smooth.Stat(0.005),
        # # exp_smooth.Stat(500),
        # pid.Stat(0.1, 0.9, 0.001, 400),

        # # # for 100k events
        # # exp_smooth.Stat(0.05),
        # # exp_smooth.Stat(50),
        # pid.Stat(0.5, 0.5, 0.001, 200),

        # # for 10k events
        exp_smooth.Stat(0.05),
        # exp_smooth.Stat(50),
        pid.Stat(0.6, 0.4, 0.001, 200),
        smooth.Stat(600),
    ]

    m = {str(s): [] for s in stats}

    for cnt in process(stats, iterations, get_interval):
        for s in stats:
            m[str(s)].append(cnt['avg'][str(s)])

    for s in stats:
        plt.plot(m[str(s)], label=str(s))

    plt.ylabel("HitRate")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
