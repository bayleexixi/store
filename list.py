list=["中国","北京","上海","广东"]
list.append("山东")
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list



pos1, pos2 = 2, 3

print(swapPositions(list, pos1 , pos2 ))

list1=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
A=sum(list1)
B=A/len(list1)
print("GDP总和",A)
print("平均GDP",B)

#将山东加进去，将广东写在上海前面
