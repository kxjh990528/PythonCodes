# 从一个列表中移除重复的元素，`numbers = [1, 2, 3, 2, 4, 3, 5, 6, 5]`
numbers = [1, 2, 3, 2, 4, 3, 5, 6, 5]

# 方法一：将列表转换为集合，再转换回列表以移除重复的元素（会打乱顺序）
# unique_numbers = list(set(numbers))

# print(unique_numbers)

# 方法二：遍历原列表，添加不重复的元素
# 定义一个空列表
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)
