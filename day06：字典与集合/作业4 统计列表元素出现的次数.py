"""
编写一个程序，统计给定列表中每个元素出现的次数，并将结果存储在一个字典中。
my_list = [1, 2, 3, 2, 1, 3, 4, 5, 2, 1]
#元素出现次数： {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}
"""
my_list = [1, 2, 3, 2, 1, 3, 4, 5, 2, 1]

# 方法一 遍历
# 创建一个空字典来存储元素和它们的计数
my_dict = {}

# 遍历列表中的每个元素
for i in my_list:
    # 如果元素已经在字典中，增加计数
    if i in my_dict:
        my_dict[i] += 1
    # 如果元素不在字典中，初始化计数为 1
    else:
        my_dict[i] = 1

print(my_dict)

# 课堂代码
count_dict = {}

for i in my_list:
    # 如果元素已经在字典中，增加计数
    if i in count_dict:
        count_dict[i] += 1
    # 如果元素不在字典中，初始化计数为 1
    else:
        count_dict[i] = 1

print("count_dict:::", count_dict)
