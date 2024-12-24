# (1)退出while循环
# while True:
#     userInput = input("请输入一个数字（输入q退出）：")
#
#     if userInput == 'q':
#         print("退出循环")
#         break
#
#     number = int(userInput)
#     square = number ** 2
#     print(f"{number} 的平方是 {square}")

# (2)退出for循环
# 查找1-100中第一个能整除13的非零偶数
for i in range(100):
    if i % 13 == 0 and i != 0 and i % 2 == 0:
        print("获取i值：", i)
        break
