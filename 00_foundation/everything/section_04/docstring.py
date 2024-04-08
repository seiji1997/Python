def multiply(num1, num2):
    """
    multiply num1 with num2 and return the result
    :param num1: first number that you want to multiply
    :param num2: second number that you want to multiply
    :return: num1 * num2
    """
    return num1 * num2


# .__doc__に文字列が格納されている
print(multiply.__doc__)

# help()でもDocstringを表示することができる
help(multiply)
multiply(3, 5)


# Google styleの例
# preference -> tools -> python integrated tools -> Docstringsで変更可能
def dividend(num1, num2):
    """
    num1 is divided by num2 and return the result
    Args:
        num1: number that you want to divide
        num2: number that num1 is divided by

    Returns:
        num1 / num2
    """
    return num1 / num2
