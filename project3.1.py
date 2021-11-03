list=[["姓名","年龄","性别","编号","任职公司", "薪资" ,"部门编号"],
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]
#统计每个人的平均薪资
sum=(500+501+600+700)
average=(sum/4)
print("平均薪资为",average)
#统计每个人平均年龄
sum1=(56+19+19+45)
average1=(sum1/4)
print("平均年龄为",average1)
#将刘备，45，男，220，alibaba，500,30，添加到列表中
a=["刘备", "45", "男", "220", "alibaba", "500" , "30"]
list.append(a)
#统计公司男女人数
#print(list[-1][2])

j=0
k=0
for i in range(1,6):
    #sex=input("请输入性别")
    if "男" in (list[i][2]):
        j = j + 1


    else:
        k=k+1

print("性别为男的个数为",j)
print("性别为女的个数为",k)

#不求人数
#for i in range(1,6):
#     if "男"in (list[i][2]):
#         print("性别为男")
#     else
#         print("性别为女")


#求每个部门的人数
q=0
w=0
e=0
r=0
for o in range(1,6):
    if "50" in (list[o][6]):      #if list[o]==""切片方法
        q=q+1
    elif "60" in (list[o][6]):
        w=w+1
    elif "10" in (list[o][6]):
        e=e+1
    elif "30" in (list[o][6]):
        r=r+1

print("部门编号为50的人数是",q)
print("部门编号为60的人数是",w)
print("部门编号为10的人数是",e)
print("部门编号为30的人数是",r)

