class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking!")


class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking!")


def walk_with_me(animal: Animal) -> None:
    # type() is のチェックは継承したsubclassがTrueにならないので注意
    # if type(animal) is Animal:
    # isinstance()はsubclassもTrueになる．型のチェックではこちらを使う．
    # if isinstance(animal, Animal):
    # Pythonは型には興味なく，振る舞いに興味があるため型ではなく振る舞いベースでの振り分けをする方がよい
    method = getattr(animal, 'walk', None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩(walk)できません")


if __name__ == "__main__":
    pochi = Dog("Pochi")
    # pochi = Animal("Pochi")
    walk_with_me(pochi)
