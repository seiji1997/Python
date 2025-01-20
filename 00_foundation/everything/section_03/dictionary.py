# dictionary: キーと値の組み合わせを複数保持するデータ型

fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# []にキーを指定して値を取得する
fruit_key = 'apple'
print(f"{fruit_key} is {fruits_colors[fruit_key]}")

# []にキーを指定して値を更新する(なければ作成)
fruits_colors['peach'] = 'pink'
print(fruits_colors)

# キーと値にはオブジェクトが入る．どんなオブジェクトでも入れることが可能
dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)

# nested dictionaryも同様に値を取得
print(dict_sample['four']['inner'])

# dictionaryにオーダー(順序)はない
colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)

# .keys()と.values()
for fruit in fruits_colors.keys():
    print(f'{fruit} is {fruits_colors[fruit]}')

for color in fruits_colors.values():
    # 通常値からキーを取得するのにdictionaryは使えないので，colorだけprint()しておく
    print(color)

for x in fruits_colors:
    # そのままforで回すとkeyがxに入る
    print(x)

# .items()
for fruit, color in fruits_colors.items():
    print(f'{fruit} is {color}')

