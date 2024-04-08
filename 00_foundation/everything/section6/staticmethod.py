class MyClass():

    def mymethod(self):
        MyClass.mystaticmethod()
        print("This is normal method!")

    # static methodは引数にselfを取らず，インスタンスには紐づかない
    @staticmethod
    def mystaticmethod():
        print("This is staticmethod")


c = MyClass()
# 普通のmethodはインスタンスに紐づいている
c.mymethod()
# static methodは通常クラスからアクセスする
MyClass.mystaticmethod()
# インスタンスからstatic methodをcallすることもできるが，これは無駄なのでやらない
c.mystaticmethod()

