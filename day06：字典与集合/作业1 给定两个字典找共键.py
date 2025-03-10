# 给定两个字典，找到它们共有的键存放到一个列表中

dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dict2 = {'B': 20, 'D': 40, 'E': 50}

# 方法一 遍历
key_list = []

for key in dict2:
    if key in dict1:
        key_list.append(key)

print(key_list)

# 方法二：集合操作 获取两个字典的键的交集
common_keys = list(dict1.keys() & dict2.keys())

print(common_keys)
