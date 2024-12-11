# int float str
x = 1
y = 3.14
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>

# num1 = input("请输入num1：")  # "1"
# num2 = input("请输入num2：")  # "2"
# print(num1 + num2)  # "1"+"2"

# (1)如何将数字转换为字符串
x_str = str(x)
print(x_str, type(x_str))
y_str = str(y)
print(y_str, type(y_str))

# (2)如何将字符串转为数字（前提是字符串一定是数字字符串）
# int()
# float()
s1 = "123"
s1_int = int(s1)
print(s1_int, type(s1_int))

s2 = "3.14"
s2_float = float(s2)
print(s2_float, type(s2_float))

# s3 = "100元"
# print(int(s3))

# 写法1
# num1 = input("请输入num1：")
# num2 = input("请输入num2：")
# num1_float = float(num1)
# num2_float = float(num2)
# print(num1_float + num2_float)

# 写法2
num1 = float(input("请输入num1："))
num2 = float(input("请输入num2："))
print(num1 + num2)

# 列表，字典，集合，元组
