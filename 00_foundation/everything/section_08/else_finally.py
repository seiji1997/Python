def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
        return "try"
    except ZeroDivisionError as e:
        print("0で割ることはできません")
        # エラーメッセージをprintすることが可能
        print(e)
    # except ValueError:
    #     print("数字を入力してください")
    # else:
    #     print(f"一人{int(each)}円です")
    finally:
        print("ご利用ありがとうございます")
        return "finally"


if __name__ == "__main__":
    return_value = split_bill(10000)
    print(return_value)