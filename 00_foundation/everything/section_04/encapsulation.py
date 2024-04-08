# カプセル化(encapsulation): 外からアクセスできないようにする
# outerではvalidationを書き, innerには実際のプログラムを書くことで，役割を分けることができる
def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f"{min_age}歳未満お断り")
        return

    def inner_casino_entrance():
        print("ようこそカジノへ")

    return inner_casino_entrance()


casino_entrance(27)
