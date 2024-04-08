# is演算子：同じオブジェクトかどうかを判定する
a = 1
b = 1
c = 3
d = a
e = 2 - 1  # 1
print(a is b)  # True
print(a is not c) # True
print(f"a's id: {id(a)}")
print(f"b's id: {id(b)}")
print(f"c's id: {id(c)}")
print(f"1's id: {id(1)}")

print(d is a)  # True
print(d is b)  # True

print(a is e)  # True

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"

print(hello, hello2)
print(hello is hello2)  # True

hello = "konnichiwa"
print(hello is hello2)  # False

nothing = None
print(nothing is None)
print(id(nothing))
print(id(None))