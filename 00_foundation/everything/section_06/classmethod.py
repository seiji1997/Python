class MyClass():

    classmethod_count = 0

    def mymethod(self):
        MyClass.mystaticmethod()
        print("This is normal method!")


    @staticmethod
    def mystaticmethod():
        print("This is staticmethod")


    # classmethodは引数にclsをとり，クラスとインタラクションを取ることができる．
    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is classmethod and now the count is {cls.classmethod_count}")



c = MyClass()
# 普通のmethodはインスタンスに紐づいている
c.mymethod()
# static methodは通常クラスからアクセスする
MyClass.mystaticmethod()
# インスタンスからstatic methodをcallすることもできるが，これは無駄なのでやらない
c.mystaticmethod()
# class methodも通常クラスからアクセスする
MyClass.myclassmethod()

