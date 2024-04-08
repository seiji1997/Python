# tuple (タプル): 変更できないリスト []ではなく()を使う

date_of_birth = (1990, 2, 3)

# unpack
year, month, day = date_of_birth
print(year)
print(month)
print(day)

# リスト同様にindexで値を取得できる
print(date_of_birth[0])
print(date_of_birth[-1])
print(date_of_birth[1:])
