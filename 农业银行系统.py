import random

# 判断输入是否为大于0的整数
def notnum(num):
    try:
        num = int(num)
        if num >= 0:
            return False
        else:
            return True
    except ValueError:
        return True

# 取字典键值
def numkey(dict):
    return ''.join(dict.keys())

# 输入数字
def innum(s):
    temp = input('请输入%s'%s)
    while notnum(temp):
        print('输入不合法，请重新输入')
        temp = input('请输入%s'%s)
    return int(temp)

# 打印账号信息
def printuser(user):
    info = '''
------------个人信息------------
用户名 : %s
账号 : %s
账户类型 : %s
取款密码 : %s
地址信息 :
国籍 : %s
省份 : %s
街道 : %s
门牌号 : %s
余额 : %s
开户行名称 : %s
    '''
    print(info % (users[user]['姓名'],
                  user,
                  users[user]['账户类型'],
                  users[user]['密码'],
                  users[user]['国家'],
                  users[user]['省份'],
                  users[user]['街道'],
                  users[user]['门牌号'],
                  users[user]['存款余额'],
                  users[user]['开户行'])
          )

# 界面
def jiemian():
    print('*'*28)
    print('*',' '*1,'中国农业银行账户管理系统',' '*1,'*')
    print('*'*28)
    print('*',' '*9,'选项',' '*10,'*')
    print('*',' '*9,'1.开户',' '*8,'*')
    print('*',' '*9,'2.存钱',' '*8,'*')
    print('*',' '*9,'3.取钱',' '*8,'*')
    print('*',' '*9,'4.转账',' '*8,'*')
    print('*',' '*9,'5.查询',' '*8,'*')
    print('*',' '*9,'6.再见',' '*8,'*')
    print('*'*28)

# users = {'账号':
#              '',
#               { '姓名':''}, {'密码': ''}, {'地址': ''}, {'存款余额': ''}, {'开户行': ''}
#               ]
#          }
users = {}

# 开户
def add_users():
    inusers1 = {}
    zhanghao = str(random.randint(0, 99999999)).zfill(8)
    print('您的账号为', zhanghao)
    while 1:
        usertype = input('请选择账户类型[1:金卡，2：普通会员卡]')
        if usertype == '1' or usertype == '2':
            break
    xingming = input('请输入姓名')
    while 1:
        mima = input('请输入6位整数密码')
        if len(mima) == 6:
            if notnum(mima):
                print('密码输入不合法，请重新输入')
            else:
                break
        else:
            print('密码输入不合法，请重新输入')
    mima = int(mima)
    guojia = input('请输入国籍')
    shengfen = input('请输入省份')
    jiedao = input('请输入街道')
    menpai = input('请输入门牌号')
    money = innum('预存金额')
    inusers1[zhanghao] = {'账户类型':usertype,'姓名':xingming,'密码':mima,'国家':guojia,'省份':shengfen,
                            '街道':jiedao,'门牌号':menpai,'存款余额':money,'开户行':'中国农业银行的昌平沙河支行'}
    status = adduser(inusers1)
    if status == 3:
        print("银行库已经满了！请携带证件到其他银行办理！")
    elif status == 2:
        print("不允许重复开户！")
    elif status  == 1:
        print("恭喜，开户成功！")
        printuser(zhanghao)
    return

# 添加用户
def adduser(dict):
    if len(users) >= 100:
        print('用户数量到达上限，添加用户失败')
        return 3
    for i in users.values():
        if dict[numkey(dict)]['姓名'] in i['姓名']:
            print('用户已存在')
            return 2
    users.update(dict)
    return 1

# 换行输出字典
def printdict(dict):
    for i in dict:
        print('{%s:%s}'%(i,dict[i]))

# 存款
def save_money():
    dict = {}
    dict['账号'] = input('请输入账号')
    money = innum('存款金额')
    dict['存款金额'] = money
    status = savemoney(dict)
    if status:
        print("存款成功")
        printuser(dict['账号'])
    else:
        print('没有该用户，存款失败')
    return

# 添加存款
def savemoney(dict):
    if dict['账号'] not in users.keys():
        return False
    else:
        users[dict['账号']]['存款余额'] += dict['存款金额']
        return True

# 取款
def with_draw():
    dict = {}
    dict['账号'] = input('请输入账号')
    mima = innum('密码')
    dict['密码'] = mima
    money = innum('取钱金额')
    dict['取钱金额'] = money
    status = withdraw(dict)
    if status == 1:
        print('没有该账户，取钱失败')
    elif status == 2:
        print('密码错误，取钱失败')
    elif status == 3:
        print('余额不足，取钱失败')
    elif status == 0:
        print('取钱成功')
        printuser(dict['账号'])
    return

# 执行取款
def withdraw(dict):
    if dict['账号'] not in users.keys():
        return 1
    elif dict['密码'] != users[dict['账号']]['密码']:
        return 2
    elif dict['取钱金额'] > users[dict['账号']]['存款余额']:
        return 3
    else:
        users[dict['账号']]['存款余额'] -= dict['取钱金额']
        return 0

# 转账
def Transfer():
    dict = {}
    dict['账号1'] = input('请输入转出的账号')
    mima1 = innum('转出账号密码')
    dict['密码1'] = mima1
    money = innum('转账金额')
    dict['转账金额'] = money
    dict['账号2'] = input('请输入转入的账号')
    mima2 = innum('转入账号密码')
    dict['密码2'] = mima2
    status = transfer(dict)
    if status == 1:
        print('没有该账户，转账失败')
    elif status == 2:
        print('密码错误，转账失败')
    elif status == 3:
        print('余额不足，转账失败')
    elif status == 0:
        print('转账成功')
        printuser(dict['账号1'])
        printuser(dict['账号2'])
    return

# 执行转账
def transfer(dict):
    if dict['账号1'] not in users.keys() or dict['账号2'] not in users.keys():
        return 1
    elif dict['密码1'] != users[dict['账号1']]['密码'] or dict['密码2'] != users[dict['账号2']]['密码']:
        return 2
    elif dict['转账金额'] > users[dict['账号1']]['存款余额']:
        return 3
    elif users[dict['账号1']]['账户类型'] == '1':
        if dict['转账金额'] > 50000:
            return 3
        else:
            users[dict['账号1']]['存款余额'] -= dict['转账金额']
            users[dict['账号2']]['存款余额'] += dict['转账金额']
            return 0
    elif users[dict['账号1']]['账户类型'] == '2':
        if dict['转账金额'] > 20000:
            return 3
        else:
            users[dict['账号1']]['存款余额'] -= dict['转账金额']
            users[dict['账号2']]['存款余额'] += dict['转账金额']
            return 0

# 查询
def Query():
    dict = {}
    dict['账号'] = input('请输入账号')
    mima = innum('密码')
    dict['密码'] = mima
    query(dict)
    return

# 执行查询
def query(dict):
    if dict['账号'] not in users.keys():
        print('该用户不存在')
        return
    elif dict['密码'] != users[dict['账号']]['密码']:
        print('密码不正确')
        return
    else:
        printuser(dict['账号'])
        # print('当前账号:',dict['账号'])
        # printdict(users[dict['账号']])

# 主程序
while 1:
    jiemian()
    num = input('请选择业务')
    while notnum(num):
        print('输入不合法，请重新输入')
        num = input('请选择业务')
    num = int(num)
    if num == 1:
        add_users()
    elif num == 2:
        save_money()
    elif num == 3:
        with_draw()
    elif num == 4:
        Transfer()
    elif num == 5:
        Query()
    elif num == 6:
        print('*',' '*6,'欢迎下次使用',' '*6,'*')
        exit()
    else:
        print('输入不合法，请重新输入')