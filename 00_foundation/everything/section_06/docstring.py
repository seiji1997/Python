class Duck:
    """
    This is a class for Duck.

    Attributes:
        name (str): the name of the duck

    Methods:
        walk: print xxx
        quack: print xxx
        fly: print xxx
    """

    def __init__(self, name):
        """
        The constructor for Duck class.
        :param name: the name of the duck
        """
        self.name = name

    def walk(self):
        """
        print walking,,,
        :return: None
        """
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
    print(help(Duck))
    print(help(Duck.__init__))
    print(Duck.__doc__)