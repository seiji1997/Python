# mode=a (append): ファイルの最後尾に内容を追加
with open("writing_file.txt", mode='a') as f:
    f.write("mode=a appends text")

# mode=r+: 読み書きどちらも可能
with open("writing_file.txt", mode='r+') as f:

    f.write("You can write and read with r+ mode!!")
    # .read()で読み込むことも可能，すると，positionが最後尾に移動する(読み込みによりpositionが移動しているから)
    print(f.read())
    f.write("This should be the last sentence")

# mode=w+: 読み書きどちらも可能．Truncateされることに注意
with open("writing_file.txt", mode='w+') as f:
    # read()も可能だが，truncate(つまりファイルのbyteは0)されているので，読み込むものはない
    print(f.read())
    f.write("You can write and read with w+ mode!!")
    f.write("The content should be truncated")
    # positionが最後になってしまっているので，.seek(0)でpositionを先頭に戻す
    f.seek(0)
    # 書き込んだものをread可能
    print(f.read())

# mode=a+: 読み書きどちらも可能で，positionが最後尾から始まり，truncateされない
with open("writing_file.txt", mode='a+') as f:
    # read()も可能だが，positionが最後尾になっているので読み込むものはない
    print(f.read())
    f.write("\nYou add sentences to the last of the file content with a+ mode!!")
    # positionが最後になってしまっているので，.seek(0)でpositionを先頭に戻す
    f.seek(0)
    # 書き込んだものをread可能
    print(f.read())
