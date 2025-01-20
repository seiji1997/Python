# 関数の定義

# 例: 華氏を摂氏に変換する
fahrenheit = 72
celsius = (fahrenheit - 32) * 5/9

print(f"華氏{fahrenheit}度は摂氏{celsius:.2f}度です")


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius = fahrenheit_to_celsius(fahrenheit)
print(f"華氏{fahrenheit}度は摂氏{celsius:.2f}度です")