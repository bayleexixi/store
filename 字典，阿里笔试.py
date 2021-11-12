def listNum(a):
    sep = list(set(a))
    dict1 = dict.fromkeys(sep, 0)
    x = 0
    while x < len(sep):
        dict1[sep[x]] = a.count(sep[x])
        x = x + 1
    return dict1


a = [21, 21, 21, 56, 56, 56, 56, 56, 56, 10, 10, 10, 10, 3, 5]
print(listNum(a))