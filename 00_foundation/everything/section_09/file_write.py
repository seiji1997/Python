# ファイルに書き込むにはmode='w'で開く
with open("writing_file.txt", mode='w') as f:
    # ファイルへの書き込みにはf.write()を使う
    # ファイルがなければ作成され，あれば上書きされる
    f.write("You can write contents here \nuse 'backslash n' to break the row")
    f.write("New write() doesn't break row")
    # print(file=)を使って書き込むことも可能
    print("You can add a new row using 'file' parameter", file=f)
    print("new print() method breaks the row for you!", file=f)
    print("new print() method breaks the row for you!", file=f)
    print("new print() method breaks the row for you!", file=f)
    # mode='w'を指定すると，readできないので注意
    # print(f.read())