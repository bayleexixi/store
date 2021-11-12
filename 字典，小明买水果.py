

dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key

for i in dict:
    print(i)

#2、请循环遍历出所有的value
for i in dict:
    print(dict[i])


#3、请在字典中增加一个键值对,"k4":"v4"
dict['k4']= 'v3'



#小明去超市购买水果，账单如下
#苹果  32.8
#香蕉  22
#葡萄  15.5

#请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
#用水果名称做key，金额做value，创建一个字典
'''
info = {
    '苹果':32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
while 1:
    fruit = input('请输入水果名称：')
    price = input('请输入该水果的价格：')
    info[fruit] = price
    print(info)
'''
#小明，小刚去超市里购买水果
#小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
#以姓名做key，value仍然是字典
Friuts = {
	"苹果":12.3,  # 水果和单价
	"草莓":4.5,
    "香蕉":6.3,
    "葡萄":5.8,
    "橘子":6.4,
    "樱桃":15.8
}
dict={}
name=input("谁")
#开始买东西
list=[]#创建一个空列表放入水果的钱
dict[name]={'fruits':{},"money":0}#创建已名字为键
while True:
    b=input("买什么")#苹果、草莓
    if b in Friuts:#往键里面添加值
        #  先找字典——》名——》购物车.更新（{你输入的购买的水果,水果的价格}）
        dict[name]['fruits'].update({b:Friuts[b]})#如果没有创建，存在就添加
        #dict[name]['fruits']={b:Friuts[b]}#如果没有创建，如果存在就重写
    if b=="1":#输入”1“退出
        break
#  循环 购物车
#    i是键
for i in dict[name]['fruits']:
    #               键的值
    list.append(dict[name]['fruits'][i])#放入列表
#   谁   在  dict就放入谁的值
if name in dict:
    # 先找字典——》名——》money=
    dict[name]["money"]=sum(list)
print(dict)
#sum是求和
#if list.count() == 3:
#统计某个内容的次数   返回一个整型 int   如重复4   返回 4:int

# for i in enumerate(dict):
#     print(dict[name]['fruits'][i])