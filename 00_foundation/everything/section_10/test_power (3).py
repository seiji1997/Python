import pytest

from power import power, times


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8
    with pytest.raises(TypeError):
        power("3", "2")


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6




# if __name__ == "__main__":
#     unittest.main()