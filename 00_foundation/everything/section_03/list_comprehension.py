# リスト内包表記(list comprehension)

# リスト内包表記を使わない書き方
square_list = []
for i in range(10):
    square_list.append(i ** 2)

print(square_list)

# リスト内包表記を使った書き方
square_list = [i ** 2 for i in range(10)]
print(square_list)

# if文を後ろにつけることでフィルタすることが可能
even_square_list = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_square_list)
