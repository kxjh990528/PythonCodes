"""
1.遍历数据的元素并操作
2.有效循环次数的构建
    内置函数range()
"""

# 案例1
# for i in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
#     print("hello world")

# 案例2
# range(start=0,end,step=1)
# 假如是range(10)，他会生成一个类似列表的结构，[0,1,2,3,4,5,6,7,8,9]
# for i in range(10):
#     # print(i)
#     print("hello world")

# 案例3
# range(start=0,end,step=1)
# for i in range(1, 101):
#     print(i)

# 案例4
# range(start=0,end,step=1)
# for i in range(1, 101, 1):
#     print(i)

# for i in range(1, 101, 2):
#     print(i)

# step默认为1，如果是正数，范围是从小到大，如果是负数，范围就是从大到小
# for i in range(100, 1, 1):
#     print(i)
# for i in range(100, 1, -1):
#     print(i)
for i in range(1, 100, -1):
    print(i)

