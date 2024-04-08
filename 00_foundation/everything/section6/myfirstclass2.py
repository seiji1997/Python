class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} is walking")


john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')

# インスタンス変数: インスタンスに紐づいている変数
# インスタンスに「.」を続けてアクセス可能
print(john.name)
john.walk()
taro.walk()

# インスタンス変数の上書き
print(f"変更前:{john.age}")
john.age = 29
print(f"変更後:{john.age}")
# 当然他のインスタンスのageには影響はない
print(f"{taro.name}のageは{taro.age}のまま")