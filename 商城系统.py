'''
商城系统：
    列表：容器来存储数据
    for循环：遍历数据
    if...else：
1.技术选型：

2.需求
    1.准备一个货架，摆上很多商品
    2.准备一个空的购物车
    3.钱包还的有钱


    4.买东西
        1.如果有这个商品
            判断余额足够买这个东西
                够买
                    余额减去商品的价格
                    购物车添加这个商品
                    温馨提示：成功添加购物车！
                不够：
                    穷鬼，买啥？？？
                是否输入的是q或者Q:
                    退出！
        2.如果没有这个商品
            温馨：没有这个商品，别瞎弄！


    5.打印购物小条！


任务1：
    改造购物小条，将多条重复显示，优化成 yyyyyyy   xn
'''

import random
discount=random.randint(1,5)
number=discount*0.1
print("您收到一张优惠券",number)
shop = [
    ["牙膏",21.5],
    ["lenovo",4500],
    ["Mac pro",12000],
    ["Iphone 18 max Pro",56000],
    ["海尔洗衣机",2500],
    ["辣条",3],
    ["洗衣粉",25],
    ["利群",160],
    ["红塔山",130]
]

mycart = []  # 空的购物车

# 初始化余额
salary = input("请输入您的钱包余额：") # "356"  -->  356
sal = salary = int(salary)   # "356" --> 356


while True:
    # 展示商品架
    for key,value in enumerate(shop):
        print(key,value)

    chose = input("请输入您要买的商品编号：") # "9aa" --> 9
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("温馨提示：这个商品不存在！别瞎弄！")
        else:
            if salary < shop[chose][1]:
                print("温馨提示：穷鬼，没钱，别瞎买！")
            else:
                salary = salary - number*(shop[chose][1])
                mycart.append(shop[chose])
                print(shop[chose][0],"添加购物车成功！余额还剩:￥",salary)
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("兄弟，商品不存在！别瞎弄！")


# 打印购物小条
print("----------------欢迎下次光临Jason小商店--------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
for key,value in enumerate(mycart):
    print(key,value)
print("-------------------------------------------------")
print("您本次还剩余额为：￥",salary,"，本次消费：￥",(sal - salary))
print("您本次购物折扣为: ",number)