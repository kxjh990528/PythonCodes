# 获取两个数字中较小的数值

# 版本1：
# num1 = int(input("num1："))
# num2 = int(input("num2："))
#
# if num1 < num2:
#     print("较小值：", num1)
# else:
#     print("较小值：", num2)

# 版本2：
num1 = int(input("num1："))
num2 = int(input("num2："))

if num2 < num1:
    num1, num2 = num2, num1
print("较小值：", num1)
