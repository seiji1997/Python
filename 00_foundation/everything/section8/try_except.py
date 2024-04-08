def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        each = price
        print("0で割ることはできません")
        # エラーメッセージをprintすることが可能
        print(e)
    except ValueError:
        each = price
        print("数字を入力してください")
    print(f"一人{int(each)}円です")


if __name__ == "__main__":
    split_bill(10000)