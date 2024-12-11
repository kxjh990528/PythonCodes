# 引导用户输入一个邮箱格式字符串，比如`916852314@163.com`或`1052065088@qq.com`等，然后将邮箱号和邮箱类型名打印出来，比如邮箱号`916852314`和`163邮箱`

# 引导用户输入
user_input = input('请输入邮箱号码：')

# 邮箱标识
mail_mark = '@'

mail_parts = user_input.split('@')

email_code = mail_parts[0]
email_type = mail_parts[1]

if mail_mark not in user_input:
    print('邮箱格式不合法')
else:
    print(f'邮箱号：{email_code}')
    if email_type == 'qq.com':
        print('邮箱类型：QQ邮箱')
    if email_type == '163.com':
        print('邮箱类型：163邮箱')
    else:
        print('暂未收录该邮箱')
