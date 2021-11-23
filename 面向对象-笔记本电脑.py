class computer:
    screen = 0
    price = 0
    cpu = ""
    memory = ""
    standby = ""
    def wate(self,watename):
        print(watename)
    def playgame(self,playgamename):
        print("屏幕大小为", self.screen, "的电脑在打", playgamename)
    def film(self,filmname):
        print("屏幕大小为", self.screen, "的电脑在看", filmname)
c = computer()
c.screen = 10.0
c.price = 10000
c.cpu = "GTX"
c.memory = "520G"
c.standby = "12小时"
c.wate("4399小游戏")
c.playgame("大鱼吃小鱼")
c.film("蜡笔小新")