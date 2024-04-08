# =================local scope=================
def print_name_local():
    first_name = 'Taro'
    last_name = 'Yamada'
    print(f"I'm {first_name} {last_name}")


print_name_local()

# =================global scope=================
age = 30


def print_age():
    # この時first_nameはlocal scopeとなる
    age = 20
    print(f"I'm {age} years old")


print_age()
# global scopeのageは関数内で変更されていない
print(age)
# global scope
age = 30

