fruits = ['apple', 'peach', 'grapes', 'banana']

# else:はfor文が回り切ったら実行
for fruit in fruits:
    choice = input(f"あなたが探しているフルーツは{fruit}ですか？ y/n:")
    if choice == 'y':
        print("見つかってよかったですね")
        break
    else:
        print("そうですか．．．")
else:
    print("お探しのフルーツは見つかりませんでした．")

# else:は条件がFalseになったら実行
balance = 1000
game_price = 200
while balance >= game_price:
    choice = input(f"1回{game_price}円のゲームに参加しますか？(残高{balance}円)(y/n):")
    if choice == 'y':
        balance -= game_price
    elif choice == 'n':
        print("また遊びましょう")
        break
    else:
        print("yかnで答えてください")
else:
    print(f"あなたの残高は{balance}円です．もうお金なくなっちゃいましたね^^")
