# range(start, stop, step)
for i in range(10):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(4, 13, 2):
    print(i)

# Challenge (FizzBuzz)
for i in range(1, 51):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 数字を使わない場合は_とする
for _ in range(5):
    print("hello!")
