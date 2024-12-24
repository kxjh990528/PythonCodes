"""
打印一个nxn的矩阵，每个元素的值等于其所在行数和列数之和。
"""
# 获取用户输入
n = int(input("请输入矩阵的大小 n: "))

for i in range(1, n+1):  # 行数从 1 到 n
    for j in range(1, n+1):  # 列数从 1 到 n
        print(i + j, end=" ")  # 打印当前元素，并以空格分隔
    print()  # 打印完一行后换行

