# if文のNoneの取り扱い
a = None
# 以下のようにせずに
if a is None:
    print("a is None")
else:
    print("a has a value")

# 以下のようにする
if not a:
    print("a is None")
else:
    print("a has a value")
