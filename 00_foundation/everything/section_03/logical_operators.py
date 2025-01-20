# 論理演算子 logical operators
# and, or, not
a = 1
b = 1
c = 10
d = 100
first_condition = a == b
second_condition = c > d
print(first_condition)  # True
print(second_condition)  # False

print(first_condition and second_condition)  # False
print(first_condition or second_condition)  # True
print(not first_condition)  # False

# challenge1
age = 13
height = 140

print(age >= 10 and height >= 110)

# challenge2
master = False
job_experience = 6
print(master or job_experience >= 5)

# 左側の評価で結果がわかる場合は右側は評価されない
print(10 > 3 or undefined == 20)
