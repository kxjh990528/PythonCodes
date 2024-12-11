# 引导用户输入一个字符串，保证长度一定是4的倍数，不足位补`=`

# 引导用户输入一个字符串
user_input = input("请输入一个字符串：")

# 计算输入字符串的长度
length = len(user_input)

# 计算需要补充的 `=` 的数量
remainder = length % 4
if remainder != 0:
    # 补充 `=` 直到长度是4的倍数
    user_input += '=' * (4 - remainder)

# 输出最终的字符串
print("最终字符串:", user_input)
