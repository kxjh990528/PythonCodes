# 编写一个程序，将两个字典合并，并将相同键对应的值进行加法运算。
dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'B': 10, 'D': 20, 'C': 30}

# 遍历字典1
for key, val in dict1.items():
    # 如果键已经在字典2中，值相加
    if key in dict2.keys():
        dict2[key] = dict2[key] + dict1[key]
    # 如果键不在字典2中，新增键值对
    else:
        dict2[key] = val

print(dict2)

# AI优化
dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'B': 10, 'D': 20, 'C': 30}

# 遍历字典1
for key, val in dict1.items():
    # 如果键已经在字典2中，值相加
    if key in dict2:
        dict2[key] += val
    # 如果键不在字典2中，新增键值对
    else:
        dict2[key] = val

print(dict2)

# 课堂讲解
# dict1.update(dict2)  # key全覆盖，值覆盖
# 最好不要操作原字典
merge_dic = dict1.copy()

for key, val in dict2.items():
    if key in merge_dic:
        merge_dic[key] += val
    else:
        merge_dic[key] = val

print("合并的字典：", merge_dic)
