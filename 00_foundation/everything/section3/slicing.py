even = [2, 4, 6, 8, 10, 12]
# 「:」を使って，複数の要素をとってくることができる(slicing)
# 基本は[開始:未満]
print(even[1:4])

# 以下二つは同じ
print(even[0:4])
print(even[:4])

# 以下二つは同じ
print(even[3:5])
print(even[3:-1])

# index3から最後の要素まで取得
print(even[3:])

# 全ての要素を取得
print(even[:])

# 文字列にも同様
text = "hello world"
print(text[3:])

# [開始:未満:step]
print(text[2:10:2])

# [::-1]とすると逆順になる
print(text[::-1])
