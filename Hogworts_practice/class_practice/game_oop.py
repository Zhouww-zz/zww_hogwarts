class Game:
    #双方血量通过传参传入
    def __init__(self,my_hp,enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp
        self.my_power = 200
        self.enemy_power = 300
    def fight(self):
        # 定义初始变量
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break
    #子类可以直接调用父类中的方法，不被重写的方法
    def rest(self,time_num):
        print(f"休息{time_num}分钟")

class HouYi(Game):

    #重写父类的构造函数
    #父类构造函数中需要传参，因此子类中重写构造函数也需要传参
    def __init__(self,my_hp,enemy_hp):
        super().__init__(my_hp, enemy_hp)
        self.defense=10
        #继承父类的构造函数


    def fight(self):
        # 定义初始变量
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break

houyi = HouYi(2000,1001)
houyi.fight()
#调用父类中的方法
houyi.rest(10)
