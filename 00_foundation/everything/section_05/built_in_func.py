# dir()で，今アクセス可能なオブジェクトやattributeの一覧を取得できる
print(dir())
# オブジェクトを入れると，そのオブジェクトのattributeの一覧を取得できる
print(dir("1"))
# __builtins__を入れると，built in の関数やattributeの一覧を取得できる
print(dir(__builtins__))