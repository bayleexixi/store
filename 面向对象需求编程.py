class student:
    number = ""
    username = ""
    aeg = 0
    sex = ""
    height = 0
    weight = 0
    achievement = 0
    address = ""
    telephon = ""
    def study(self,time):
        print(self.username, "正在学习,已经学习了", time, "小时！")
    def playGame(self,game):
        print(self.username,"喜欢打游戏，正在玩【",game,"】timi")
    def baincheng(self,rows):
        print(self.username,"正在写代码，已经写了",rows,"行")
    def sumname(self,ber):
        sums = sum(ber)
        print("求和的结果为：",sums)

s = student()
s.username = "希希"
s.study(10)
s.playGame("英雄联盟")
s.baincheng(12)
ber = [0,1,2,4,7,9]
s.sumname(ber)