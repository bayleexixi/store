shop = {
                    "板栗", "山楂", "熏鸡", "烤鸭"
                }
city = {
    "北京":{
        "海淀":{
            "高校":["清华","北大"],
            "公园":["香山","植物园"],
            "博物馆":["军事博物馆","国家地质公园"]
        },
        "昌平":{
            "景点":["八达岭长城"],
            "回龙观":["永旺","北科"]
        }
    },
    "上海":{
        "上海滩":{
            "景点":["迪士尼乐园"]

        }
    }
}
def showCity(data):
    for i in data:
        print(i)

while True:
    print("-------------------欢迎来到baylee旅行社-----------------")
    print ("有以下城市可以去: ")
    showCity(city)
    print("请输入您要去的城市: ")
    chose = input("")

    if chose == "q" or chose == "Q":
        print("欢迎下次光临!")
        break
    elif chose not in city:
        print("输入非法!请重新输入: ")
    else:
        showCity(city[chose])
        chose2 = input("请输入您要去的二级城市: ")
        if chose2 == "q" or chose2 == "Q":
            print("欢迎下次光临!")
            break
        elif chose2 not in city[chose]:
            print("输入错误")
        else:
            showCity(city[chose][chose2])
            print("请输入要去的具体景点: ")
            chose3=input(" ")
            if chose3 == "q" or chose2 == "Q":
                print("欢迎下次光临!")
                break
            elif chose3 not in city[chose][chose2]:
                print("输入错误")
            else:
                showCity(city[chose][chose2][chose3])
                print("每张票500/人!")
                h=input("是否买纪念品?")
                if h =="是":
                    print("请输入您要买的纪念品: ")
                    print(shop)
                    chose = input("")
                    print("购买成功 ")
                elif chose == "q" or chose == "Q":
                    print("欢迎下次光临!")
                    break
                elif chose not in shop:
                    print("没有该商品")
                else:
                    break
    break


