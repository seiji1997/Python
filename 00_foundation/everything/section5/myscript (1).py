# 標準ライブラリ, サードパーティライブラリ, 自分たちのライブラリ, ローカルのファイルという順に書く
# ※それぞれをabc順に書き，1行空ける
# 基本的にはscriptの最初に書く
# import sys, mymoduleと一行で書かないこと
import sys

import mymodule  # as mmとすると，as以降に指定した名前でアクセスすることができるが，一般的なもの以外には使わない方が良い
# from mymodule import myfuncでもOK
# from mymodule import myfunc, anotherfuncと書くのはOK
# from mymodule import * でもimportできるが非推奨
# import * では，_ から始まるnonpublicな関数はimportできない
# その場合myfunc()と関数名に直性アクセスすることができる
# が，このやり方だとそれぞれの関数や変数がどのモジュールからきたのかがわかりにくいので注意が必要

# mymodule.xxの形でグローバル変数や関数にアクセスできる
mymodule.myfunc()
print(mymodule.global_variable)

# sys.pathには，カレントディレクトリや環境変数のPYTHONPATHに設定されているパスが入っている
print(sys.path)

# Pythonが読み込む先のパスを追加したければ，sys.path.append()で追加すればよい
sys.path.append("/Users/me/Desktop/UdemyPython/Function/")
import docstrings
docstrings.multiply(5, 10)