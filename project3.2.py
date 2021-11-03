a=0
b=0
c=0
d=0
list=["罗恩", 23 ,35 ,44]
list1=["哈利" ,60, 77 ,68 ,88, 90]
list2=["赫敏", 97 ,99 ,89 ,91, 95, 90]
list3=["马尔福" ,100, 85 ,90]
for i in range(1,len(list)):
    a=a+list[i]
for i in range(1,len(list1)):
    b=b+list1[i]
for i in range(1,len(list2)):
    c=c+list2[i]
for i in range(1,len(list3)):
    d=d+list3[i]
print("罗恩的总成绩为",a)
print("哈利的总成绩为",b)
print("赫敏的总成绩为",c)
print("马尔福的总成绩为",d)
