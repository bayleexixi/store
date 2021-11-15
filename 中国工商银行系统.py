import random
bank_name = "中国工商银行昌平沙河支行"
bank = {}



#  展示各项业务
def welcome():
    print("------------------------------------")
    print("-    中国工商银行账户管理系统        -")
    print("------------------------------------")
    print("-  1.开户                          -")
    print("-  2.存钱                          -")
    print("-  3.取钱                          -")
    print("-  4.转账                          -")
    print("-  5.查询                          -")
    print("-  6.Bye!                          -")
    print("------------------------------------")

def liu():
    mima = input("请输入密码")
    while len(mima) != 6:
        print("请输入六位数密码")
        mima=input("请输入密码")
    return mima

# 银行的开户方法
def bank_AddUser(account,username,password,country,province,street,door,money):
    # 判断银行库是否已满
    if len(bank) > 100:
        return 3

    if account in bank:
        return 2

    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    print(bank)
    return 1





# 开户方法
def addUser():
    # 姓名(str)、密码(int:6位数字)、地址、存款余额(int)
    username = input("亲输入您的姓名：")
    password= input("亲输入您的取款密码：")

    country = input("亲输入您国籍：")
    province = input("亲输入您的省份：")
    street = input("亲输入您的街道：")
    door = input("亲输入您的门牌号：")
    money = int(input("亲输入您的初始账户余额："))

    account =  random.randint(10000000,99999999)

    # 调用银行的开户方法
    status = bank_AddUser(account,username,password,country,province,street,door,money)
    if status == 3:
        print("银行库已经满了！请携带证件到其他银行办理！")
    elif status == 2:
        print("不允许重复开户！")
    elif status  == 1:
        print("恭喜，开户成功！")
        info = '''
            ------------个人信息------------
            用户名 : %s
            账号：%s
            取款密码 : %s
            地址信息：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额:%s
            开户行名称：%s
        '''
        print(info % (account,username,password,country,province,street,door,money,bank_name))





def AddMoney1(account,money1 ):
    if account in bank:
        bank[account]["money"]+=money1
    else:
        print("没有该用户！")
        return False



def choosemoney(account,password,money2):
    if account in bank:
        if bank[account]["password"] == password:
            bank[account]["money"] = bank[account]["money"] - money2
            print("取款成功")
            print(bank)
            return 0
        else:
            print("密码错误")
            return 2
    elif money2>bank[account]["money"]:
        print("余额不足!")
        return 3
    else:
        print("账户不存在")
        return 1



def  transfer(account,account1,password,money3):
    if account in bank:
        if bank[account]["password"] == password:
            bank[account]["money"] = bank[account]["money"] - money3
            bank[account1]["money"] = bank[account1]["money"] + money3
            print("转账成功")
            print(bank)
            return 0
        else:
            print("密码错误")
            return 2
    elif account1 not in bank:
        print("账号不存在")
        return 1
    else :
        money3 > bank[account]["money"]
        print("余额不足！")
        return 3


def demand(account,password):
    if account in bank:
        if bank[account]["password"] == password:
            print(bank)
            return
        else:
            print("密码错误")
            return
    else:
        print("账户不存在")
        return








while True:
    welcome()
    chose = input("请输入业务编号：")

    if chose == "1":
        addUser()
    elif chose == "2":
        account = int(input("账号"))#int类型
        money1 = int(input("存款金额为: "))
        print("存款成功!")
        AddMoney1(account,money1)
    elif chose == "3":
        account = int(input("账号"))
        password = liu()
        money2= int(input("取款金额为: "))
        choosemoney(account,password,money2)

    elif chose == "4":
        account = int(input("账号"))
        account1 = int(input("转入账号"))
        password = liu()
        money3= int(input("转账金额为: "))
        transfer(account,account1,password,money3)

    elif chose == "5":
        account = int(input("账号"))
        password = liu()
        demand(account,password)
    elif chose == "6":
        break
    else:
        print("输入错误！请重新输入！")