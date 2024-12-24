"""
编写一个程序，判断一个字符是否为元音字母（a、e、i、o、u，包括小写和大写）。
如果是元音字母，则输出"是元音字母"，否则输出"不是元音字母"。
"""

vowels = "aeiou"  # 定义所有的小写元音字母

char = input("请输入一个字母：")  # 获取用户输入

# 统一转化为小写比较
if char.lower() in vowels:
    print(f'{char}是元音字母')
else:
    print(f'{char}不是元音字母')
