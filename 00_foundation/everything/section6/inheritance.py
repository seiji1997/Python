class Animal(object):
    def __init__(self, name):
        self.name = name
        print('Animal init is called')

    def breath(self):
        print(f"{self.name} is breathing!!")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# subclassのインスタンスを生成するときに，superclassのAnimalのコンストラクタが呼ばれている
dog = Dog("pochi")
cat = Cat("tama")

dog.breath()
cat.breath()
