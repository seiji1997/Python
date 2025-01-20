def even(num):
    while num!=0:
        if num % 2 == 0:
            yield num
        num -= 1


# 自作のgenertorもnext()で値を返し，iter()でiteratorを返している．
# generatorはiteratorの一種
even10 = even(10)
print(next(even10))
print(iter(even10))


