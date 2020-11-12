class Bicycle:
    def run(self,km):
        print(f"用脚骑行了{km}公里")

# bike=Bicycle()
# bike.run(20)
#EBicycle继承自Bicycle，定义类时在后面加括号，写入父类名称
class EBicycle(Bicycle):

    #用构造函数进行传参
    def __init__(self,valume):
        print(f"电瓶车初始电量为{valume}")
        self.valume=valume

    #构造充电函数，电量通过参数传入
    def fill_charge(self,vol):
        self.valume=self.valume+vol
        print(f"充了{vol}度电充电后电量为{self.valume}")

    #相当于重写了父类中的run方法
    def run(self,km):
        power_km=self.valume*10
        if power_km >= km:
            print(f"我用电瓶电量骑行了{km}公里")
        else:
            print(f"我用电瓶电量骑行了{power_km}公里")
            #这里是非继承调用
            # bike=Bicycle()
            # bike.run(km-power_km)
            #继承调用
            super().run(km-power_km)

ebike=EBicycle(20)
ebike.fill_charge(10)
ebike.run(1000)

