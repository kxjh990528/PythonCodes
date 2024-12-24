"""
编写一个程序，生成斐波那契数列的第20个数字（斐波那契数列是指从0和1开始，后面的每一项都是前两项的和）
0 1 1 2 3 5 8 ....
"""

# 计算斐波那契数列的第 n 项
# 初始化前两个数字
# a = 0
# b = 1
#
# # 循环计算斐波那契数列的第 20 个数字
# for i in range(2, 21):  # 从第 2 个数字开始到第 20 个数字
#     a, b = b, a + b
#
# # 输出第 20 个数字
# print(f"斐波那契数列的第 20 个数字是：{b}")

# 课堂讲解代码
pre = 0
current = 1
for _ in range(1, 19):  # 因为前两个已经有了所以到19就够了
    next_num = pre + current
    print("next：", next_num)
    pre = current
    current = next_num
