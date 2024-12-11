# x = 1
# y = x
# x = 2
# print(x)
# print(y)

# 如何交换两个变量值
a = 1
b = 2
# 方式1
temp = a
a = b
b = temp
print(a, b)
# 方式2
a, b = b, a
print(a, b)
