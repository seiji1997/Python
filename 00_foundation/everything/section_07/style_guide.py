# 変数定義
# Correct:
xxx = 1
y = 2
# Wrong:
xxx           = 1
y             = 2

# 無駄に行の最後にスペースを入れない(エディタによっては見えないので注意)
x = 1

# 引数の「=」にはスペース不要
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# operatorの周りにスペース一個．もしオペレータのpriorityがある場合は無くす
# Correct:
x = x + 1
x += 1
x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# Wrong:
x=x+1
x +=1
x = x * 2 - 1
a = x * x + y * y
c = (a + 1) * (a - 1)

# コンマの後にはスペースを入れる．
# Correct:
range(1, 11)
# Wrong:
range(1,11)
# しかし，そのあとに閉じカッコが来る場合はスペース不要
# Correct:
foo = (0,)
# Wrong:
bar = (0, )

# 要素を並べる時にコンマで終えることが可能．そうすることで簡単に行を追加でき，gitなどのバージョン管理で差分にならない
# ただこれをやる場合は，閉じカッコは次の行にすること
# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
# Wrong:
FILES = ['setup.cfg', 'tox.ini',]

# PEPでは一行79文字までを推奨しているが，厳密にやる必要はない
# 高解像度化により80文字は全然フィットするようになってきている．
# (pycharmのデフォルトは120文字)
# 関数名が長くて折り返す場合は，
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
# のように引数のはじまりの縦をあわせるか
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
# のように引数を全てインデントするか
# ※この場合一行目の引数は書かない．つまり以下はNG
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# 関数定義の際に改行する場合は，二行目を8スペース開けることでその次のブロックとの差がわかるようにする
# correct
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# ブロックの境目がわからなくなるのはNG
# wrong
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# '\'で区切って改行する

print("このように表示する文章がながったりした場合は \
バックスラッシュで区切ると改行できます")
# 演算子の後ではなく，前で改行する．
# Correct:
a = 10000000000000000 \
    + 100000000000000 \
    + 10000 \
    + 10000

# Wrong:
b = 10000000000000000 +\
    100000000000000 +\
    10000 +\
    10000


# 関数間は2行空ける
def func():
    pass


def func2():
    pass


# メソッド間は1行空ける
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

# importはファイルの最初に書く
# importは別々の行に書く
# Correct:
import os
import sys

# Wrong:
import sys, os

# ただfromをつける場合は一行にまとめてOK.(でないと大量のimport文を書くことになる)
# Correct:
from subprocess import Popen, PIPE

# 書く順番は
# 1.Standard library
# 2.Third party
# 3.Our library
# 4.Local library
# それぞれ1行空ける

# なるべくabsolute importを使う
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# 長すぎたらNG
from package.subpackage1.subpackage2.subpackage3.module4 import function

# コメント
# ・コメントは常に最新にする．コメントとコードの中身が異なるなら，コメントは無い方がまし
# ・なるべく英語で書く．絶対に日本語がわからない人が読むことがないなら英語で書く必要はない
# ・書くときは文章で書くのが望ましい
# ・# のあとに半角スペースを入れる
# ・Docstringは基本的に全てのmodule, function, class, methodにつける(non publicな外からアクセスしない関数には不要)
# ・そのコードが「なにをしているか」より「なぜそう書いたか」の方が有益

# 命名規則(naming convention)
# 変数名や関数(メソッド)名: snake_case 例) balance, image_height
# クラス名: CamelCase 例) Person, MyClass
# モジュールやパッケージ名: なるべく短いlower caseで，必要であればsnake_case 例) time, numpy

# アンダースコア
# - _xxx internal use only(non public)の意味
# - xxx_ Pythonで既に使われている単語を使いたいとき．(例:type_
# - __xxx クラスの属性として使うことで名前修飾される
# - __xxx__ magic methodと呼ばれるもので，Pythonが特別に設定しているもの．開発者定義することはない．(overrideすることはある)
# - _: 最近実行した戻り値や，iteration時に使わない変数

# l, I, Oという一文字の変数名は1や0に見間違えるので使わないこと
# Correct:
length = len(letter)
# Wrong:
l = len(letter)

# Constants(宣言後変更しない変数)は大文字のsnakecaseを使う
PI = 3.14
# 変更は可能なので注意(Pythonでは強制できない)
PI = 3

# returnを書くなら全部書く．書かないなら一個も書かない.
# Correct:
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

# Wrong:
def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)

# オブジェクトタイプの確認はisinstance()を使う
# Correct:
if isinstance(obj, int):
# Wrong:
if type(obj) is type(1):

# Booleanに比較演算子は使わない
bool_var = True
# Correct:
if bool_var:

# Wrong:
if bool_var == True:

# Type hints
# function定義時にannotationをつけて
def greeting(name: str) -> str:
    return 'Hello ' + name
# のように型のヒントを与えることができる．
# ・一つでもhitをつけたら全てにつける．
# ・typeのチェックをするわけではない
# ・Pythonは動的型付言語であることを意識すること
# ・このtype hintを強制したり，命名規約に入れるべきではない

