from power import power, times


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8, "this should be 8"


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6, "this should be 6"


if __name__ == "__main__":
    test_power()
    test_times()