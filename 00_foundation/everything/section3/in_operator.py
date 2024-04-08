fruits = ['apple', 'peach', 'grapes', 'banana']
print('apple' in fruits)
print('lemon' not in fruits)

# challenge
favorite = input("好きなフルーツはなんですか？")

if favorite in fruits:
    print("{}ですね．差し上げますよ".format(favorite))
    fruits.remove(favorite)
else:
    print("{}ですね．仕入れました！".format(favorite))
    fruits.append(favorite)

print("今あるフルーツはこちらです.{}".format(fruits))
