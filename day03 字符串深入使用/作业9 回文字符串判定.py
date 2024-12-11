# 引导用户输入一个字符串，判断是否是回文字符串

# 引导用户输入一个字符串
user_input = input('请输入一个字符串：')

if user_input == user_input[::-1]:
    print(f'{user_input}是一个回文字符串')
else:
    print(f'{user_input}不是一个回文字符串')