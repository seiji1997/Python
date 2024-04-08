class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')

# インスタンス変数: インスタンスに紐づいている変数
# インスタンスに「.」を続けてアクセス可能
print(john.name)