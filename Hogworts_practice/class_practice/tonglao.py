class TongLao:

    hp=1000

    def __init__(self,power):
        self.power=power

    def see_people(self,name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self,enemy_hp,enemy_power):
        self.hp = self.hp*10
        self.power = self.power/2
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp- self.power

        if final_hp > enemy_final_hp:
            print("天山童姥赢了")
        else:
            print("天山童姥输了")

if __name__ == "__main__":
    tonglao=TongLao(100)
    tonglao.see_people("李秋水")
    tonglao.fight_zms(10000,500)

