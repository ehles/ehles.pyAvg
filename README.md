# pyavg

`pyavg` is a Python library that provides a set of classes for calculating averages from input data using various methods. It supports both basic and specialized smoothing and filtering algorithms.

---

## Installation

You can install the library via PyPI:

```bash
pip install ehles.pyavg
```

## Key Features

The library offers classes for different average calculation methods, including:

1. Basic Moving Average (bi_avg.Stat)
2. Cumulative Average (cumulative.Stat)
3. Exponential Smoothing (exp_smooth.Stat)
4. PID Controller-Based Average (pid.Stat)
5. Ring Buffer for Averaging (ring_buff.Stat)
6. Advanced Smoothing Algorithms (smooth.Stat)

Each class implements a common interface, making it easy to switch between methods as needed.

## Usage Examples

### Basic Moving Average

```python
from pyavg import BiAvgStat

# Create an object for moving average calculation
stat = BiAvgStat(window_size=5)

# Add values
stat.add(10)
stat.add(20)
stat.add(30)

# Get the current average
print(stat.get_average())  # -> 20.0
```

### Cumulative Average

```python
from pyavg import CumulativeStat

# Create an object for cumulative average calculation
stat = CumulativeStat()

# Add values
stat.add(10)
stat.add(20)
stat.add(30)

# Get the current average
print(stat.get_average())  # -> 20.0
```

### Exponential Smoothing

```python
from pyavg import ExpSmoothStat

# Create an object for exponential smoothing
stat = ExpSmoothStat(alpha=0.5)

# Add values
stat.add(10)
stat.add(20)
stat.add(30)

# Get the current smoothed value
print(stat.get_average())  # -> smoothed value
```

## Documentation

Each class provides the following key methods:

- `add(value: float):` adds a new value to the calculation.
- `get_average() -> float:` returns the current average.

For details on implementation and additional parameters, refer to the source code or library documentation.

## Requirements

- Python 3.6 or higher.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contribution

If you’d like to contribute or add a new average calculation method, feel free to submit a Pull Request or reach out through [GitHub Issues](https://github.com/ehles/ehles.pyAvg/issues).
