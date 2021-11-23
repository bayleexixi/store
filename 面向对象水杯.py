'''水杯 属性：高度，容量，颜色，材质
能存放液体
'''
class glass:
    high = 0
    color = ""
    V = 0
    color = ""
    data = ""

    a = ""
    def use(self):
        print(self.a,"的杯子")
    def show(self):
        print("我的高度是",self.high,"米，我是",self.color,"的，我的材质是",self.data,"的，我的体积是",self.V,"升。")
c=glass()
c.high =1
c.color = "红色"
c.data = "玻璃"
c.V = 2.5

c.a = "baylee装水"

c.use()
c.show()


