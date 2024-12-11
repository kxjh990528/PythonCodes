# 用户输入一个11位手机号，将第5位至第8位替换成`*`

# 用户输入号码
phone_num = input('请输入一个11位数的手机号：')

# 判断是否是数字
if len(phone_num) == 11 and phone_num.isdigit():
    # 替换第5到第8位
    print(phone_num[:4]+'****'+phone_num[8:])
else:
    print('请输入有效的11位手机号！')
