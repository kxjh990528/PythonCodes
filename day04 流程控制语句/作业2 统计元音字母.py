"""
统计元音字母：编写一个程序，接受用户输入的一段文本，统计其中元音字母（a、e、i、o、u）的个数，并输出结果。
"""

vowels = "aeiou"  # 定义所有的小写元音字母
count = 0  # 初始化计数器

# 获取用户输入的文本
text = input("请输入一段英文文本：")

# 遍历文本中的每个字符
for i in text:
    # 如果字符是元音字母，忽略大小写
    if i.lower() in vowels:
        count += 1

# 输出结果
print(f"文本中元音字母的个数是：{count}个")

