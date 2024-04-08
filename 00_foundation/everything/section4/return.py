# returnしない関数を作ることもできる
def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key: {k}, value: {v}")


a = {"one": 1, "two": 2}
print(a)
print_dict(a)

# returnしない関数は，Noneをreturnしている．
return_value = print_dict(a)
print(return_value)  # None


# 複数returnする場合は,(カンマ)で区切って渡す
def get_first_last_word(text):
    text = text.replace(",", "")
    words = text.split()
    return words[0], words[-1]


text = "Hello, My name is Mike"
# 複数戻り値があると，tuppleで渡されるので，unpackで受け取る
first, last = get_first_last_word(text)
print(f'first word is {first}, last word is {last}')

