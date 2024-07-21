import unittest
from datetime import datetime
from calculate_intervals_and_remainder import calculate_intervals_and_remainder

class TestCalculateIntervalsAndRemainder(unittest.TestCase):

    def test_basic_case(self):
        entered = datetime(2023, 10, 30, 17)
        left = datetime(2023, 10, 30, 18, 31)
        self.assertEqual(calculate_intervals_and_remainder(entered, left), (3, 60))
    
    def test_no_interval_case(self):
        entered = datetime(2023, 10, 30, 17)
        left = datetime(2023, 10, 30, 17, 15)
        self.assertEqual(calculate_intervals_and_remainder(entered, left), (0, 900))
    
    def test_exact_interval_case(self):
        entered = datetime(2023, 10, 30, 17)
        left = datetime(2023, 10, 30, 18)
        self.assertEqual(calculate_intervals_and_remainder(entered, left), (2, 0))
    
    def test_invalid_interval(self):
        entered = datetime(2023, 10, 30, 17)
        left = datetime(2023, 10, 30, 18)
        with self.assertRaises(ValueError):
            calculate_intervals_and_remainder(entered, left, interval_minutes=0)
    
    def test_negative_interval(self):
        entered = datetime(2023, 10, 30, 17)
        left = datetime(2023, 10, 30, 18)
        with self.assertRaises(ValueError):
            calculate_intervals_and_remainder(entered, left, interval_minutes=-10)

if __name__ == "__main__":
    unittest.main()

