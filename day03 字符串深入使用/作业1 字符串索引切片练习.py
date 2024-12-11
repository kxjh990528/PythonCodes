s = "hello world"

# 操作1：通过正反索引切片world
print(s[6:])
print(s[-5:])

# 操作2: 获取world的翻转,即"dlrow"
# print(s[:-6:-1])
print(s[6:][::-1])