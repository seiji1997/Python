class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        print("get_age called")
        return self._age

    def set_age(self, age):
        print("set_age called")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age = age

    age = property(get_age, set_age)


john = Person("John", 10)
# john.set_age(-10)
john.age = -10
print(john.age)
john._age = -10
print(john.age)