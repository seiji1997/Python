# mutable: 変更可能なオブジェクト list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f"fruitsのIDは{id(fruits)}")
fruits.append('lemon')
print(fruits)
print(f"lemonが追加されてもfruitsのIDは{id(fruits)}")

# immutable: 変更不可能なオブジェクト int, float, str, bool, tuple
fruit = 'apple'
print(f"fruitのIDは{id(fruit)}")
fruit += ', lemon'
print(fruit)
print(f"lemonが追加されたfruitのIDは{id(fruit)}")

# 効率が悪い: strはimmutableなので，text += '-' + str(i)は別の変数を作っている
# ※Pythonは賢いので，ループの中ではstrを"時々"mutableのように扱うことがある．
text = ""
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# 効率が良い: listはmutableなので，毎回のループで新しい変数を作ることはせず，同じ変数を更新していく
text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)