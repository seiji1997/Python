# 0で割るとエラーがでる
# result = 100 / 0

# 前の行でエラーが出ていると実行されない
print("Hello world")

# これもエラーになる. strは自動でintに型変換されない
# result = "1" + 3
# strをintに型変更させる．(またはintをstrにさせる)
# result = int("1") + 3

# 定義(宣言)していない変数を参照するとエラーになる
print(undefined_variable)
