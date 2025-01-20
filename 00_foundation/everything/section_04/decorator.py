# Decorator: 関数に機能を付属する(デコレートする)
def greeting(func):
    def inner(*args, **kwargs):
        print("Hello!")
        func(*args, **kwargs)
        print("Nice to meet you!")

    return inner


@greeting # say_name = greeting(say_name)と同じ
def say_name(name):
    print(f"I'm {name}")


say_name("Jiro")
# say_name = greeting(say_name)
# print(say_name)
# say_name("Jiro")


@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")


# say_name_and_origin = greeting(say_name_and_origin)
# say_name_and_origin("Jiro", "Tokyo")

say_name("Taro")
say_name_and_origin(name="Jiro", origin="Tokyo")
