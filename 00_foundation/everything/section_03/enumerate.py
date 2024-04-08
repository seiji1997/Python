fruits = ['apple', 'peach', 'grapes', 'banana']

for idx, fruit in enumerate(fruits):
    print(f"index: {idx}, fruit: {fruit}")

for x in enumerate(fruits):
    # xはtuple型
    print(x)
