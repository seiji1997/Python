# Pythonは参照渡し
def add_nums(a, b):
    print(f"第一引数のID:{id(a)}")
    print(f"第二引数のID:{id(b)}")
    return a + b


one = 1
two = 2
# oneは1, twoは2というオブジェクトを参照している
print(id(one))
print(id(two))
# add_nums内でも1, 2というオブジェクトを参照しているのでidは同じ
add_nums(one, two)


# immutableでは変数を更新できないので値渡しのような挙動をする
def add_one(num):
    print(f"変更前のID:{id(num)}")
    num += 1
    print(f"変更後のID:{id(num)}")
    return num


one = 1
print(id(one))
print(f'関数呼び出し前のone:{one}')
add_one(one)
print(f'関数呼び出し後のone:{one}')


# mutableでは変数を更新できるので(そのまま)参照渡しの挙動となる
def add_fruit(fruits, fruit):
    print(f"変更前のID:{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")
    return fruits


myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'
print(f'関数呼び出し前のmyfruits{myfruits}')
add_fruit(myfruits, myfruit)
print(f'関数呼び出し後のmyfruits{myfruits}')

# mutableは
