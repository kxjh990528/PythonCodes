# 编写一个程序，将列表中的所有字符串元素反转
# 原始列表
words = ["hello", "world", "python", "is", "awesome"]

# 方法一：遍历列表
# reverse_words = []
# for word in words:
#     reverse_words.append(word[::-1])

# print(reverse_words)

# 方法二：列表表达式
reverse_words = [word[::-1] for word in words]
print(reverse_words)
