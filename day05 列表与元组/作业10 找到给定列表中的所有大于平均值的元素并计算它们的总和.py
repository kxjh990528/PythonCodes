# 编写一个程序，找到给定列表中的所有大于平均值的元素并计算它们的总和
# 定义列表
numbers = [3, -1, 4, 1, -5, 9, 2, 6]

# 方法一：遍历
# 计算平均值
average = sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# 新定义列表存储大于平均值的元素
above_nums = []
# 大于平均值元素的总和
sum_above_aver = 0
# 遍历列表
for num in numbers:
    if num > average:
        above_nums.append(num)
        sum_above_aver += num

print("大于平均值的元素的列表：", above_nums)
print("大于平均值的元素的和：", sum_above_aver)


