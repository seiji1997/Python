import json

# json.loadでjsonファイルをpythonのデータ構造で読み込み
with open("example.json") as f:
    data = json.load(f)

print(data)
print(data['glossary']['GlossDiv'])

# json.dumpでpythonのデータをjsonファイルに書き込み
new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open("new_json.json", 'w') as f:
    json.dump(new_json, f)

with open("new_json.json", 'r') as f:
    new_json_reload = json.load(f)

print(new_json_reload)
# タプルはリストになってjsonに保存されるので，再度読み込むとリストとなって読み込まれていることに注意
# 書き込んで再度読み込んだら同じになるとは限らない
print(new_json_reload['key2'])

# json.dumpsでpythonのデータ構造をjsonの文字列に変換する
json_str = json.dumps(new_json)
print(json_str)
print(type(json_str))
# json.loadsで，jsonの文字列をpythonのデータ構造に変換する
python_data = json.loads(json_str)
print(python_data)
print(type(python_data))
