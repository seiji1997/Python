fruits = ['apple', 'lemon', 'peach']

# リストをnext()に入れてもエラーになる
# next(fruits)

# iter()関数でiteratorを返す
fruits_iter = iter(fruits)

# iteratorはnext()で値を返す
print(next(fruits_iter))

# iteratorはiter()関数でiterator(自分自身)を返す
print(id(fruits_iter))
fruits_iter_iter = iter(fruits_iter)
print(id(fruits_iter_iter))

# next()は__next__()と等しい
print(next(fruits_iter))
print(fruits_iter.__next__())
