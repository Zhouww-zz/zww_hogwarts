import random


def fight(enemy_hp,enemy_power):

    #定义初始变量
    my_hp=1000
    my_power=200
    print(f"敌人的血量为{enemy_hp}，敌人的攻击力为{enemy_power}")
    #建立循环，使游戏可以进行多轮回合
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        if my_hp <= 0 :
            print(f"我方剩余血量为{my_hp}，敌方剩余血量为{enemy_hp}\n我输了")
            break
        elif enemy_hp <= 0 :
            print(f"我方剩余血量为{my_hp}，敌方剩余血量为{enemy_hp}\n我赢了")
            break
#当前文件可以执行下列代码，如果是将该包导入到其他项目中，下面的代码不会被执行
if __name__ == "__main__":
    #使用列表推导式随机获取血量列表中的值
    hp=[x for x in range(990,1010)]
    enemy_hp=random.choice(hp)
    print(enemy_hp)
    #使用randint随机获取在一个区间里的整数型
    enemy_power=random.randint(190,210)
    print(enemy_power)

    fight(enemy_hp,enemy_power)