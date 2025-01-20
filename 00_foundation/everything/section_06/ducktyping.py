class Duck:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack..!!")

    def fly(self):
        print("Whee!!")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack..??")

    def swim(self):
        print("Swimming!!")


if __name__ == "__main__":
    donald = Duck("Donald")
    pingu = Penguin("Pingu")
    # 「Penguinクラスでも，.walk()と.quack()をするならDuckとして扱ってもよい」という考え方がダックタイピング
    donald.walk()
    pingu.walk()
    donald.quack()
    pingu.quack()

