# 列表元素求和：编写一个程序，计算给定列表中所有元素的和，
# 但要跳过列表中的负数，`numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]`
numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]

# 方法一：遍历列表
# 计算总和
# num_sum = 0

# for num in numbers:
#     if num >= 0:
#         num_sum += num
#
# print(num_sum)

# 方法二：列表表达式
# 使用列表推导式来计算总和，跳过负数
num_sum = sum(num for num in numbers if num >= 0)

print(num_sum)
