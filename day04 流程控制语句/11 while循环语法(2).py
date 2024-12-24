"""
# 准备：
# 假设有一个变量s的初始值为0，将s增加5次，每次增加值分别为1，2，3，4，5，然后打印s的值。
"""

# 实现代码
count = 1  # 初始语句
s = 0
while count <= 100:  # 判断条件
    # s = 0  # 会怎么？
    print("count:::", count)
    s += count
    count += 1  # 步进语句

print(s)