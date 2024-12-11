# `names='yuan rain eric alvin'`,**引导用户输入一个名字，判断是否在这个名字字符串中，是打印True，不是打印False

# 定义名字字符串
names = 'yuan rain eric alvin'

# 引导用户输入一个名字
input_name = input("请输入一个名字: ")

# 判断名字是否在字符串中
if input_name in names:
    print(True)
else:
    print(False)
