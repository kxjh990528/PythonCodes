"""
双分支语句的语法 if-else

if 表达式：
    语句1
    语句2
    语句3
else:
    语句4
    语句5
    语句6
"""

# 案例1：获取用户年龄
age = int(input("请输入您的年龄:"))

# 判断是否进入成年电影
if age >= 18:
    print("进入成人电影院！")
    print("欧美区")
    print("日韩区")
    print("国产区")
else:
    print("进入青少年模式！")
    print("科幻冒险类")
    print("益智早教类")
    print("科普记录类")