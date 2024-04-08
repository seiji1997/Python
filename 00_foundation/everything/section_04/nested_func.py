# 関数の中で関数を定義(nested function)
def outer():
    def inner():
        print("this is inner function")
    inner()


outer()
inner()  # -> エラーになる．定義されていないのでアクセスできない


# inner関数はouter関数の変数にアクセス可能
def outer(outer_param):
    def inner():
        print(f"this is inner function, and I can access to {outer_param}")
    inner()


outer("arg")


# outer関数はinner関数のローカル変数にアクセスはできない
def outer():
    def inner():
        inner_variable = "inner var"
        print("this is inner function")
    inner()
    print(inner_variable)  # -> エラーなる

outer()

# global変数とlocal変数とnonlocal変数
msg = "I am global"


def outer():
    msg = "I am outer"

    def inner():
        nonlocal msg #msgはnonlocal変数となる
        msg = "I am inner"
        print(msg)
    inner()
    print(msg)


print(msg)
outer()
