# 有些程序经常需要引导用户输入"Y"或"N"，其中"Y"代表肯定，"N"代表否定。
# 无论用户输入大写的"Y"还是小写的"y"，结果都被视为肯定。肯定打印True

# 引导用户输入
in_str = input("是否确认？(Y/y)表示确认：")

# 方法一：判断是大写还是小写y
if in_str == "Y" or in_str == "y":
    print(True)
else:
    print(False)

# 方法二：统一转换大写
print(in_str.upper() == 'Y')