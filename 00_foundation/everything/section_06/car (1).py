class Car(object):

    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print("{0.manufacturer}の{0.model_name}(燃費:{0.mileage}),アクセル全開!!".format(self))

    def brakes(self):
        print(f"{self.manufacturer}の{self.model_name}(燃費:{self.mileage}),ブレーキ！!!")


if __name__ == "__main__":
    conti_gt = Car("Bentley Continental GT", 4, "Bentley")
    prius = Car("Prius", 20, "TOYOTA")

    conti_gt.gas()
    prius.brakes()