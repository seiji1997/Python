# + 演算子でリストを結合する

print([1, 2, 3] + [4, 5, 6])

# appendすると要素として追加されるので，二重リストになることに注意
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)


a = [1, 2, 3]
b = [4, 5, 6]
# a = a + b
a += b
print(a)
