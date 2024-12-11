# 引导用户输入一个手机号,通过一个逻辑表达式判断该字符串是否符合电信手机号格式，格式要求如下，是打印True，不是打印False
# 要求1: 输入的长度必须是11位
# 要求2: 输入内容必须全部是数字
# 要求3: 前三位是133或153（电信号段）

# 引导用户输入一个手机号
phone_number = input("请输入手机号：")

# 判断手机号是否符合电信格式
is_valid = (len(phone_number) == 11 and
            phone_number.isdigit() and
            (phone_number.startswith('133') or phone_number.startswith('153')))

# 输出结果
print(is_valid)