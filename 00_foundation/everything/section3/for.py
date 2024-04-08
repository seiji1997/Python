fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print("I love {}!!".format(fruit))

# Challenge1
favorite = input("好きなフルーツは？")
for fruit in fruits:
    if fruit == favorite:
        print("I love {}!!".format(favorite))
    else:
        print("{}は別に普通...".format(fruit))


# Challenge2
favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    choice = input(f"{fruit}は好き? y/n")

    if choice == 'y':
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"favorite fruits: {favorite_fruits}")
print(f"normal fruits: {normal_fruits}")
