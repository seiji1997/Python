# 通常値を取るには[]を使えばOK
fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
print(fruits_colors['apple'])

# 存在しないキーを指定するとエラーになる
# print(fruits_colors['peach'])

# in演算子 を使って，キーが存在するかを確認することができる
if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print("the key is not found")

#.get()を使うのが良い
fruit = input("フルーツの名前を指定してください")
print(fruits_colors.get(fruit, 'Nothing'))

# .update()
fruits_colors2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_colors.update(fruits_colors2)
print(fruits_colors)

