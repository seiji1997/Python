class Person(object):

    # クラス変数はclassのトップレベルに定義
    num_legs = 2
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking... with {Person.num_legs} legs!")


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

# クラス変数はインスタンス間で共有する
print(john.num_legs)
print(taro.num_legs)

# クラス変数は<Class名>.に続けてアクセスできる
print(Person.num_legs)

# クラス変数をクラス経由で変更すると，
print("Person.num_legs = 3 を実行")
Person.num_legs = 3
# 全インスタンスでそれが共有される
print(john.num_legs)
print(taro.num_legs)
# インスタンス経由で更新すると，そのインスタンスの変数だけが更新される
# ※他の言語と挙動が異なるので注意．またクラス変数をインスタンス経由で更新することは普通はしない
# warningもでないので注意．バグのもとになる
john.num_legs = 4
print("john.num_legs = 4を実行")
print(john.num_legs)
print(Person.num_legs)
print(taro.num_legs)

print(f"create {Person.count} persons!!")
