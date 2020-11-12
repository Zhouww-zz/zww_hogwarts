# class House():
#     #静态变量，可在类中调用也可在对象中调用
#     door="red"
#     floor="red"
#
#     #构造函数，在类实例化的时候直接执行
#     #此处的self是指方法中必须至少有一个参数，self是约定俗成的一种方式，是每个实例化对象的主人
#     def __init__(self):
#         #调用静态变量需要加self
#         print(self.door)
#         #实例变量,在类中，方法中，以”self.变量名“定义，在该类的其他方法中以self.变量名直接引用，
#         # 因为构造函数在实例化的时候已经执行了
#         self.kitchen="cook"
#     #定义方法
#     def sleep(self):
#         #类当中，方法当中调用，普通变量
#         bed="席梦思"
#         #在方法中以self.变量名定义的变量是全局变量，在整个类中有效，
#         # 但是如果在别的方法中调用，则必须先执行定义该变量的方法
#         #所以为了方便可以将全局变量直接定义在构造函数中，实例化时自动执行
#         self.table="桌子是黄色的"
#         print(f"可以在房子里躺在{bed}上睡觉")
#
#     def cook(self):
#         print(f"可以在房子里做饭吃{self.bed}")
# #把类实例化
# north_house=House()
# china_house=House()
# #调用实例化当中的方法
# north_house.sleep()



