"""
编写一个程序，接受用户输入的一个整数，判断该数是否是素数（只能被1和自身整除的数）。
注意，素数的定义是大于1的自然数，只能被1和自身整除，没有其他的正因数。
"""

# 获取用户输入
# num = int(input("请输入一个整数："))
#
# # 判断是否是素数
# if num <= 1:
#     print(f"{num} 不是素数，因为素数必须大于1。")
# else:
#     # 假设 num 是素数
#     is_prime = True
#     # 只需要判断到 sqrt(num)，因为如果 num 可以被大于 sqrt(num) 的数整除，那必定也能被小于 sqrt(num) 的数整除
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} 是素数。")
#     else:
#         print(f"{num} 不是素数。")

# 课堂讲解代码
# 方案一
# num = int(input("请输入一个大于1的整数："))
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         print(f"{num}不是素数")
#         break
#
# if flag:
#     print(f"{num}是素数")

# 方案二（补充）：for-else
"""
for item in sequence:
    # 迭代操作
    if condition:
        # 满足条件时执行的操作
        break
else:
    # 在循环结束后执行操作
"""
num = int(input("请输入一个大于1的整数："))

for i in range(2, num):
    if num % i == 0:
        flag = False
        print(f"{num}不是素数")
        break

else:
    print(f"{num}是素数")
