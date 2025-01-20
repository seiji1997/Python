class MyClass(object):
    # pass
    def __str__(self):
        return "MyClassの__str__"


mc = MyClass()
print(mc)  # mc.__str__()の返り値をprintしている

#argにboolを入れてもstrを入れても機能する
# argがintなのかboolなのかはpythonのコードを実行する時に決定される
def printvalue(arg):
    print(arg + 1)


varius_types = [1, "1", True, [1], (1,), {'1': 1}, {1}]
for elem in varius_types:
    # 型がなんであろうと，printableであれば実行可能．ポリモーフィズムのおかげで，ループで回すことができる
    print(elem)