import unittest
from power import power, times


class TestMyMethods(unittest.TestCase):

    def test_power(self):
        base = 2
        exp = 3
        self.assertEqual(power(base, exp), 8)
        with self.assertRaises(TypeError):
            power("3", "2")

    def test_times(self):
        num1 = 2
        num2 = 3
        self.assertEqual(times(num1, num2), 6)




# if __name__ == "__main__":
#     unittest.main()