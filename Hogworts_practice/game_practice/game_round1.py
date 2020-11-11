
def fight():

    #定义初始变量
    my_hp=1000
    enemy_hp=1000
    my_power=200
    enemy_power=200

    #定义血量值计算方法
    my_final_hp=my_hp-enemy_power
    enemy_final_hp=enemy_hp-my_power

    #三目运算
    print("我输了") if my_final_hp < enemy_final_hp else print("我输了")

    #传统写法
    # if my_final_hp < enemy_final_hp:
    #     print("我输了")
    # elif my_final_hp > enemy_final_hp:
    #     print("我赢了")
    # else :
    #     print("平局")
#调用函数
fight()
