#12月份销售总金额
import xlrd

year = xlrd.open_workbook(filename=r"C:\Users\lenovo\Desktop\day8\2020年每个月的销售情况.xlsx", encoding_override=True)
sheet_num = len(year.sheets())
'''
总销售额计算
'''
sale_sum = 0
for i in range(sheet_num):
    sheet_num_i = year.sheet_by_index(i)
    rows_year = sheet_num_i.nrows
    for j in range(1, rows_year):
        data_year = sheet_num_i.row_values(j)
        sale_sum = sale_sum + (int(data_year[2]) * int(data_year[4]))
print('本年度总销售额为%s元' % sale_sum)

'''
各衣服销售额占比
'''
var_dict = {}
var_dict2 = {}
for x in range(sheet_num):
    sheet_num_x = year.sheet_by_index(x)
    var_len = sheet_num_x.nrows
    for y in range(1, var_len):
        var_list = sheet_num_x.row_values(y)
        if var_list[1] not in var_dict:
            var_dict[var_list[1]] = int(var_list[2]) * int(var_list[4])
        else:
            var_dict[var_list[1]] += int(var_list[2]) * int(var_list[4])
        if var_list[1] not in var_dict2:
            var_dict2[var_list[1]] = int(var_list[4])
        else:
            var_dict2[var_list[1]] += int(var_list[4])
for z in var_dict:
    print('%s的销售额占比为%.2f%%' % (z, var_dict[z] / sale_sum * 100), end=' ')
print('')

'''
各种衣服的销售件数占比
'''
var_sum = 0
for w in var_dict2:
    var_sum += var_dict2[w]
for q in var_dict2:
    print('%s的销售件数占比为%.2f%%' % (q, var_dict2[q] / var_sum * 100), end=' ')
print('')

'''
每件衣服的每月销售件数占比
'''


def month_var(sheet_month, month_len):
    month_dict = {}
    for i in range(1, month_len):
        month_list = sheet_month.row_values(i)
        if month_list[1] not in month_dict:
            month_dict[month_list[1]] = int(month_list[4])
        else:
            month_dict[month_list[1]] += int(month_list[4])
    return month_dict


month = 1
for n in range(sheet_num):
    sheet_num_n = year.sheet_by_index(n)
    month_len = sheet_num_n.nrows
    month_dict = month_var(sheet_num_n, month_len)
    month_sum = 0
    for m in month_dict:
        month_sum += month_dict[m]
        print('%s月%s的销售件数占比为%.2f%%' % (month, m, month_dict[m] / month_sum * 100), end=' ')
    print('')
    month += 1
print('')

'''
最畅销的衣服
'''
key_list = list(var_dict2.keys())
value_list = list(var_dict2.values())
max_var = max(value_list)
min_var = min(value_list)
k = value_list.index(max_var)
l = value_list.index(min_var)
print('最畅销的是%s,销售量最低的是%s' % (key_list[k], key_list[l]))

'''
每季度的畅销衣服
'''
seasons_dict = {}
spring = [2, 3, 4]
summer = [5, 6, 7]
fall = [8, 9, 10]
winter = [11, 12, 1]


def four_seasons(seasons):
    for i in seasons:
        seasons_num_i = year.sheet_by_index(i - 1)
        rows_seasons = seasons_num_i.nrows
        for j in range(1, rows_seasons):
            data_seasons = seasons_num_i.row_values(j)
            if data_seasons[1] not in seasons_dict:
                seasons_dict[data_seasons[1]] = int(data_seasons[4])
            else:
                seasons_dict[data_seasons[1]] += int(data_seasons[4])

    key_list = list(var_dict2.keys())
    value_list = list(var_dict2.values())
    max_var = max(value_list)
    k = value_list.index(max_var)
    return key_list[k]


print('春季最畅销的是%s，夏季最畅销的是%s，秋季最畅销的是%s，冬季最畅销的是%s' % (
four_seasons(spring), four_seasons(summer), four_seasons(fall), four_seasons(winter)))