# 将二维列表中所有元素放在一个新列表中，numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 原始列表
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 新列表，用来存放所有元素
# flattened_list = []

# # 遍历二维列表中的每个子列表
# for sublist in numbers:
#     # 遍历每个子列表中的元素
#     for num in sublist:
#         # 将每个元素添加到新列表中
#         flattened_list.append(num)

# 输出结果
# print(flattened_list)

# 方式2
print([j for i in numbers for j in i])
print([j for i in numbers for j in i if j % 2 == 0])
