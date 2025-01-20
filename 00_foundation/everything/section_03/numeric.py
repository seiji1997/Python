# int (Integer, 整数)
print(type(1))

# float (浮動小数点)
print(type(0.1))

# ちょうど0.3にはならないので注意
print(0.1 + 0.1 + 0.1)

# Numeric Operator (数値演算子)

# 四則演算
print(1 + 0.4)  # 1.4
print(1 - 0.4)  # 0.6
print(2 * 3)  # 6
print(1 / 2)  # 0.5 int 同士の演算でもfloatになる

print(5*6 - 3/6)  # 29.5

# floatとintの計算結果はfloatになることに注意
result = 1 + 1.0
print(f"type of result:{result} is {type(result)}")

# その他の演算
print(14 // 3)  # 4　(floor division, 整数部)
print(14 % 3)  # 2 (modulo,　剰余, 余り)
print(2 ** 3)  # 6 (exponentiation, べき乗)

# 結果を変数に代入することも可能
result = 1 + 5
print("1 + 5 = {}".format(result))

# 変数同士の演算も可能
hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is {remain}")

# augmented assignment +=, -=, *=, /=
a = 1
a += 1 # a = a + 1 と同じ
print("a is {}".format(a))

hit_point = hit_point - attack_point
hit_point -= attack_point

# floatをfstingやformatで補完するときは，小数点を指定するといい {value:width.precision}
value = 1/3
# print(f"value is {value}")  # value is 0.3333333
print(f"value is {value:.4f}")  # value is 0.3333
print(f"value is {value:.2f}")  # value is 0.33
print(f"value is {value:10.2f}")  # value is       0.33
print(f"value is {value:6.2f}")  # value is   0.33

