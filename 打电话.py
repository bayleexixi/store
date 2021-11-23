'''
人类：
属性:
姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
功能：
发短信（要求参数传入短信内容）。
打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，
若为空或者小于1元则报相对应的错误信息，否则的话拨通。
结束后，按照时间长度扣费并返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，
其他：0.65元/钟、48个积分/钟））
'''



import time
class Person:
    username = ""
    sex = ""
    aeg = 0
    balance = 0
    brand = ""
    capacity = ""
    screen = 0
    standby = 0
    interral = 0
    def message(self,content):
        print("输入短信内容",content)
    def phone(self,number,time,balance):
        if number == "Null":
            print("号码为空")
        elif balance < 1:
            print("话费余额不足")
        else:
            print("电话拨通")
            print("通话结束，通话时长为",time)
            if time >0 and time <10:
                money = time *1
                balance = balance - money
                print("通话费用为：",money,"话费余额为",balance)
            elif time >=10 and time < 20:
                money = time * 0.8
                balance = balance - money
                print("通话费用为：", money, "话费余额为", balance)
            else:
                money = time * 0.65
                balance = balance - money
                print("通话费用为：", money, "话费余额为", balance)
            return
p = Person()
p.username = "小明"
p.sex = "男"
p.aeg = 25
p.balance = 50
p.brand = "华为"
p.capacity = "1000毫安"
p.screen = 15.6
p.standby = 10
p.interral = 100
p.message("今天去吃麦当劳")
p.phone("123456789",30,50)




