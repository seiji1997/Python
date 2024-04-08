def func(first, second, third):
    print(f"first: {first}, second: {second}, third: {third}")


# 順番通りに入れる
func("1", "2", "3")  # -> first: 1, second: 2, third: 3

# 順番通りに入れない場合は引数を指定する
func("1", third="3", second="2")  # -> first: 1, second: 2, third: 3


# デフォルトの値を指定する場合は，位置引数(positional parameter)より後に書く
def func(first, second, third="3"):
    print(f"first: {first}, second: {second}, third: {third}")


func("1", "2")  # -> first: 1, second: 2, third: 3
