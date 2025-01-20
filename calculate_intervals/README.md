# Calculate Intervals and Remainder

This project provides a function to calculate the number of intervals and the remainder between two datetime objects. It is useful for scenarios like billing logic where charges are applied at specific intervals.

## Files

- `calculate_intervals_and_remainder.py`: Contains the main function and an example usage.
- `test_calculate_intervals_and_remainder.py`: Contains the unit tests for the main function.
- `logger_config.py`: Contains the logger configuration.

## Usage

### Prerequisites

Make sure you have Python installed on your system. You can install the required packages using:

```bash
pip install -r requirements.txt
```

## Main Function
The main function is calculate_intervals_and_remainder which calculates the number of intervals and the remainder in seconds between two datetime objects.

```python
from datetime import datetime
from calculate_intervals_and_remainder import calculate_intervals_and_remainder

entered = datetime(2023, 10, 30, 17)
left = datetime(2023, 10, 30, 18, 31)

intervals, remainder = calculate_intervals_and_remainder(entered, left)

print(f"Intervals: {intervals}")  # 30-minute intervals count
print(f"Remainder: {remainder} seconds")  # Remainder in seconds
```

## Running the Main Script
To run the main script, use the following command:

```shell
python calculate_intervals_and_remainder.py
```

example output

```
Intervals: 3
Remainder: 60 seconds

```


## Logging
Logging is configured in logger_config.py. It logs debug information about the calculation process.

## Unit Tests
Unit tests are provided to verify the functionality of the calculate_intervals_and_remainder function. The tests cover various cases including normal usage, no interval case, exact interval case, and invalid interval values.

## Running Unit Tests
To run the unit tests, use the following command:

```shell
python test_calculate_intervals_and_remainder.py
```
