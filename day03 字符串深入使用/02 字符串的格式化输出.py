# (1) %占位符
# name = "lin"
# age = 18
# height = 175
#
# s = """
# 姓名：%s
# 年龄：%s
# 身高：%s
# """ % (name, age, height)
# print(s)

# (2) f-str
# name = "lin"
# age = 18
# height = 175
#
# s = f"姓名：{name}，年龄：{age}，身高：{height}"
# print(s)
# name = "lin"
# age = 18
# height = 175.123456
#
# s = f"姓名：{name:^15}，年龄：{age:^20}，身高：{height:<20.5}"
# print(s)
#
# name = "abcdegf"
# age = 45
# height = 155.123456
#
# s = f"姓名：{name:*^15}，年龄：{age:<20}，身高：{height:20.5}"
# print(s)

# 补充 f-str {表达式}
name = "lin"
age = 18
height = 175

s = f"""
姓名：{name}
年龄：{age}
虚岁：{age + 1}
身高：{height}
其他1：{1 + 1}
其他2：{1 + 1 > 2}
其他3：{type(1 + 1 > 2)}
"""
print(s)
