class Person:
    def __init__(self, name):
        self.name = name
        self.__mymethod()

    def mymethod(self):
        print("Person method is called")

    __mymethod = mymethod


class Baby(Person):
    def mymethod(self):
        print("Baby method is called")


taro_baby = Baby("Taro")
print(dir(taro_baby))
p = Person("test")
p.mymethod()
taro_baby.mymethod()