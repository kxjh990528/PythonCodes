# 编写一个程序，找到给定列表中的最大值和最小值
# 定义列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 方法一：使用内置的max()和min()函数
# max_value = max(numbers)
# min_value = min(numbers)

# 方法二：遍历
# 初始化最大值和最小值
max_value = numbers[0]
min_value = numbers[0]

# 遍历列表中的每个数字
for num in numbers:
    # 如果当前数字比已知最大值更大，更新最大值
    if num > max_value:
        max_value = num
    # 如果当前数字比已知最小值更小，更新最小值
    if num < min_value:
        min_value = num

# 输出结果
print("最大值是:", max_value)
print("最小值是:", min_value)
