# ループで回す
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line)


# .read()でファイルの中身の全てを一つのstringとして返す
    # ※大きなファイルでやらないこと
with open("pep8_introduction.txt") as f:
    print(f.read())

# .readline()で一行ずつ取得しstringとして返す
with open("pep8_introduction.txt") as f:
    line = f.readline()
    row_num = 0
    while line:
        print(f"{row_num}行目", line, end='')
        line = f.readline()
        row_num += 1

# .readlines()で全ての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)
