# 案例1：计算1-100的和
# count = 1
# s = 0
# while count <= 1000:
#     # 逻辑代码块开始
#     s += count
#     # 逻辑代码块结束
#     count += 1
# print(s)

# for版本
# s = 0
# for i in range(1, 101):
#     s += i
# print(s)

# 案例2
import random
import string

char = string.ascii_letters + string.digits

# while版本
# count = 0
# randomCodes = ""
# while count < 10:
#     code = random.choice(char)
#     randomCodes += code
#     count += 1
#
# print(randomCodes)

# for版本
s = ""
for i in range(100):
    code = random.choice(char)
    s += code

print(s)
