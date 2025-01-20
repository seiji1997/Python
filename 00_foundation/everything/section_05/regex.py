import re

# 正規表現(Regular Expression　通称RegEx)

email = "myemail@gmail.com"
# in演算子を使うことで文字を含んでいるか確認できる
print("@" in email)

# re.searchを使うことで，より高度なマッチングが可能
matched = re.search('@\w+\.', email)
if matched:
    print(matched)
    print("Matched!!")

else:
    print("Not found!!")


# []
print(re.search('[abc]', 'a'))  # match
print(re.search('[abc]', 'apple'))  # match
print(re.search('[abc]', 'd'))  # no match
print(re.search('[a-c]', 'b'))  # match
print(re.search('[0-9]', '0'))  # match
print(re.search('[0-9]', '5'))  # match
print(re.search('[0-9]', 'a'))  # no match
print(re.search('[0-9]', 'a1'))  # match

# ^ は最初の文字
print(re.search('^[0-9]', '0test'))  # match
print(re.search('^[0-9]', 'test'))  # no match

# {n}はn回リピート(以下の例は最初は4桁の数字）
print(re.search('^[0-9]{4}', '2021/3/31'))  # match
print(re.search('^[0-9]{4}', '21/3/31'))  # no match
# {n,m}: 最低n回，最高m回リピート
print(re.search('^[0-9]{2,4}', '2021/3/31'))  # match
print(re.search('^[0-9]{2,4}', '21/3/31'))  # match

# $は最後の文字
print(re.search('[0-9]{2}$', '2021/3/31'))  # match
print(re.search('[0-9]{2}$', '2021/3/1'))  # no match

# *は左のパターンを0回以上繰り返す
print(re.search('a*b', 'b'))  # match
print(re.search('a*b', 'ab'))  # match

# +は左のパターンを1回以上繰り返す
print(re.search('a+b', 'ab'))  # match
print(re.search('a+b', 'a'))  # no match
print(re.search('a+b', 'b'))  # no match

# ?は左のパターンを0回か1回繰り返す
print(re.search('ab?c', 'abc'))  # match
print(re.search('ab?c', 'abbbc'))  # no match
print(re.search('ab?c', 'bc'))  # no match
print(re.search('abc?c', 'abc'))  # match

# |はor
print(re.search('abc|012', 'abc'))  # match
print(re.search('abc|012', '012'))  # match
print(re.search('abc|012', '01'))  # no match

# ()はグループ
print(re.search('te(s|x)t', 'test'))  # match
print(re.search('te(s|x)t', 'text'))  # match

# .は任意の一文字
print(re.search('h.t', 'hat'))  # match
print(re.search('h.t', 'hut'))  # match
print(re.search('h.t', 'hot'))  # match

# \はエスケープ
print(re.search('h\.t', 'h.t'))  # match

# \wは[a-zA-Z0-9_] つまりアルファベトおよび数字とアンダースコア
print(re.search('h\wt', 'hit'))  # match
print(re.search('h\wt', 'h0t'))  # match
print(re.search('h\wt', 'hiit'))  # no match
print(re.search('h\wt', 'h.t'))  # no match

# challenge1
pattern_dob = '^(20|19)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$'
while True:
    dob = input("生年月日を入力してください(yyyy/mm/dd)")
    result = re.search(pattern_dob, dob)
    if result:
        print(f"{dob}は正しいフォーマットです")
        break
    else:
        print(f"{dob}は正しくないフォーマットです")

# challenge2
pattern_email = '^(\w|\.|\-)+@(\w|\.|\-)+\.[a-zA-Z]{2,3}$'
print(re.search(pattern_email, 'tes_t.te-st@gmail.com'))
