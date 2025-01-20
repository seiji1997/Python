# =================global変数を関数内で書き換える

call_count = 0
# CALL_COUNT = 0　 # 書き換えられたくない場合は全て大文字で定義するのが一般的(constant variable)


def print_count1():
    # globalをつけると，global変数にアクセスすることができる
    global call_count
    call_count += 1
    print(f"関数1:{call_count}回目")


def print_count2():
    global call_count
    call_count += 1
    print(f"関数2:{call_count}回目")


print_count1()
print_count2()
print_count1()
print_count1()
# global scopeのcall_countが書き換えられている
print(call_count)
