# 関数(function)もオブジェクト
def compute_square(num):
    return num * num


f = compute_square
print(f)
print(type(f))  # -> <class 'function'>
print(f(10))


# なのでlistやdictionaryの要素として入れることが可能
function_list = ["1", 1, True, f]
print(function_list[-1](10))


# 関数を引数に渡したり，
def execute_func(func, param):
    return func(param)


print(execute_func(f, 10))


# 関数をreturnすることもできる
def return_func():

    def inner_func():
        print('This is an inner function')
    # ()で実行していないことに注意．この場合，関数のオブジェクトが返される
    return inner_func


f = return_func()
print(f)
print(type(f))
f()


# Closure: 状態をキープした関数を作ることができる
# 状態が静的の例
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four)
print(power_four(2))  # -> 16
print(power_four(3))  # -> 81


# 状態が動的の例
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))  # -> 5.0
print(average_nums(15))  # -> 10.0
print(average_nums(4))  # -> 8.0
print(average_nums(10))  # -> 8.5


