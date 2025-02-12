# 编写一个程序，计算给定列表中所有正数元素的平均值。

# 定义列表
numbers = [3, -1, 4, 1, -5, 9, 2, 6]

# 方法一：遍历
# 存放正数总和
positive_sum = 0
# 存放正数的个数
count = 0

# 遍历列表
for num in numbers:
    # 判断是否为正数
    if num > 0:
        positive_sum += num
        count += 1

# 防止除以 0 错误（如果没有正数时）
if count > 0:
    # 使用 f-string 保留两位小数
    print(f"正数元素的平均数是：{positive_sum / count:.2f}")
else:
    print("列表中没有正数元素。")
