global_variable = "This is grlobal variable"

def myfunc():
    print("This is my function!!")


def anotherfunc():
    print("This is another function!!")


def _internal_use_only():
    print("I'm internal use only!!")


print(f"__name__ of mymodule.py: {__name__}")
if __name__ == "__main__":
    myfunc()
    anotherfunc()
    _internal_use_only()