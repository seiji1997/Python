# リスト(lists): 複数のオブジェクトを順序づけて保存するデータ型
# []で括って，,(カンマ)で各オブジェクトを区切る
fruits = ['apple', 'peach', 'melon', 'grapes']

# 要素のデータ型はなんでもOK　リストの中にリストを入れることも可能
hetero_list = ['string', 1, 3.4, True, fruits]

# 要素を取り出すときには[]の中にindexを指定する. indexは0から始める
print(fruits[0])

# indexに負の値を指定すると後ろから数えて要素を取得する
print(fruits[-1])

# 二重リストの場合は，二度indexを指定すればOK (３重，４重も同じ)
print(hetero_list[-1][0])

# これらは文字列にも使える
print("hello world"[3])

# .append: 新しいオブジェクトを追加する
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
print(fruits)

# .remove: マッチした最初のオブジェクトを除く
fruits.remove('peach')
print(fruits)

# .sort(): 昇順に並び替える
fruits.sort()
print(fruits)

# 降順にする
fruits.sort(reverse=True)
print(fruits)

# len(): リストの要素数を取得する
print(len(fruits))

# 文字列にも使用可能
print(len('hello world'))