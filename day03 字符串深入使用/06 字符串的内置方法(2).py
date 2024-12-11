# (4) strip：去除两端的空格或者换行符
# name = input("姓名：")
# print(name)
#
# ret = name.strip()  # 去除两端的空格或者换行符
# print(ret)
# print(len(ret))

# 案例2
# print("\nlin\n")
# print("\nlin\n".strip())

# 案例3
# s = "##abcd####"
# print(s.strip("#"))
# print(s.rstrip("#"))
# print(s.lstrip("#"))

# (5) isdigit: 判断字符串是否为数字字符串
# print("apple".isdigit())
# print("123".isdigit())
# print("123元".isdigit())
# print("123.45".isdigit())
# age_str = input("age:::")

# if age_str.isdigit():
#     age = int(age_str)
#     print(age)
# else:
#     print("非法输入！")

# (6) split() 分割 和 join() 拼接
# cities = "北京 哈尔滨 重庆 大连 武汉"
# ret = cities.split(" ") # ['北京', '哈尔滨', '重庆', '大连', '武汉']
# print(ret)
# print(len(ret))
