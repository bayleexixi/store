list= ["1","5","21","30","15","9","30","24"] #引号的意思是这里的数字是字符串，
                                             # 不是int类型
sum=0
for i in range(0,len(list)):
#print(list[i])         #int 的作用是把字符串改成int型  int型才可以运算

    if int(list[i]) % 5 ==0:
        print(list[i],'是5的倍数')
        sum=sum+int(list[i])

print("5的倍数的和为",sum)




