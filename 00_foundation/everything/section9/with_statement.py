# built in であるopen()関数を使う
f = open("pep8_introduction.txt")
for line in f:
    print(line, end='')
# open後はclose()
f.close()

# try finallyを使う
try:
    f = open("pep8_Introduction.txt")
    for line in f:
        print(line, end='')
finally:
    f.close()

# 実際にはwith statementを使うのが一般的
with open("pep8_Introduction.txt") as f:
    for line in f:
        print(line, end='')
