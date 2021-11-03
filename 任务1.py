
    #实现输入10个数字，并且打印10个数的求和结果
'''i,j,k=0,0,0
while i<10:
    i+=1
    j=int(input('请输入第%s个数'%i))
    k=k+j
print(k)




    #从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''i,j,k,max=0, 0, 0,0
while i<10:
    i+= 1
    j=int(input('请输入第%s个数' %i))
    k=k + j
    average=(k/10)
    if max<j:

        max=j
print('请输入10个数的和',k)
print('平均数为',average)
print('最大的数为',max)




    #使用random模块，如何产生 50~150之间的数？
'''import random

print(random.randint(50,150))

'''

'''
    #从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''a = int(input('请输入三角形的边1：'))
b = int(input('请输入三角形的边2：'))
c = int(input('请输入三角形的边3：'))
if a < b + c and b < a + c and c < a + b:
    # print('可以形成三角形')
    if a == b == c:
        print('等腰三角形')
    elif a == b and a != c:
        print('等边三角形')
    elif a == c and a != b:
        print('等边三角形')
    elif b == c and b != a:
        print('等边三角形')
    elif a ** 2 == b ** 2 + c ** 2:
        print('直角三角形')
    elif b ** 2 == a ** 2 + c ** 2:
        print('直角三角形')
    elif c ** 2 == a ** 2 + b ** 2:
        print('直角三角形')
    else:
        print('普通三角形')
else:
    print('不能形成三角形')


'''    #有以下两个数，使用+，-号实现两个数的调换。
           #     A=56
            #    B=78
    #实现效果：
             #   A=78
              #  B=56
            
'''A = 56
B = 78
i = input('输入-后者+号')
if i == "-":
    print('A=', A, 'B=', B)
elif i == "+":
    C = A
    A = B
    B = C
    print('A=', A, 'B=', B)
else:
    print('非法输入')

    #实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''i = 0

while i < 3:
    user = input('请输入用户名：')
    password = input('请输入密码：')
    i = i + 1
    if user == 'root' and password == 'admin':
        print('登录成功')
        break
    elif i == 3:
        print('此账户已锁定')
    else:
        print('请重新输入用户名和密码！')
'''

'''
    编程实现下列图形的打印
'''i = 7
p = 0
while i > 0:                                                                                                
    j = i - 1
    p = p + 1
    print(' ' * j, ' *' * p)
    i = i - 1
'''
'''
#使用while循环实现NxN乘法表的打印。
#编程实现99乘法表的倒叙打印

                                                                                           
'''
i = 1
num = int(input('请输入数字：'))
while num > 0:
    for i in range(1, num + 1):
        print(i, '*', num, '=', i * num, end="  ")
    print('\t')
    num = num - 1
'''
#一只青蛙掉在井里了，井高20米，
#青蛙白天网上爬3米，晚上下滑2米，
#问第几天能出来？请编程求出。
'''q = 0
day = 1
num = 0
while q <= 20:
    day = day + 1
    q = q + 3
    if q >= 20:
        break
    q = q - 2
    print('青蛙', day, ' 天爬了', q, '米')
'''

    #用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
i = 20
sum = 0
num = 1
j = 20
while j > 0:
    while i >1 :
        # print(num, '*', i, '*', (i - 1))
        num =num * i * (i-1)
        i = i - 2
    # print(num)
    sum = sum + num
    num = 1
    i = j -1
    j = j - 1
print(sum)
