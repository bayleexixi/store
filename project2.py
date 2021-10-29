import random
randint_num = random.randint(1, 10)
i=0
t=1000
while i<=10:
    num = int(input("猜猜今日福利彩票蓝色号码球"))
    if num == randint_num:  # 进行判断
        print("Ok")  # 打印ok
        break  # 退出
    elif num > randint_num:
        print("你输入的过大")
    elif num < randint_num:
        print("你输入的过小")
    i=i+1
    t=t-100
    print("您猜的次数为",i)
    print("您的剩余金额为",t)
    if t<=0:
        print("您的金额不足")
        break
    decide=input('不玩了输入Q/q退出:')
    if decide.upper()=='Q':
        break
