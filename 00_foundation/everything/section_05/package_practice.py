from myfirstpackage.subdir import *
# 以下は不可
# import myfirstpackage.module1.myfunc
# 以下でも可
# from myfirstpackage.module1 import myfunc
# from myfirstpackage import module1

# 同じ名前の関数でも，名前空間が異なる
# myfirstpackage.module1.myfunc()
# myfirstpackage.myfunc()
myfunc()
myfunc2()