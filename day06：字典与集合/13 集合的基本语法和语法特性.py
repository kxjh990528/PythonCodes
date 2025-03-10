s1 = {1, 2, 3}
print(type(s1))  # <class 'set'>
print(len(s1))

# (1) 无序
# s1[0]

# (2)唯一特性
s2 = {1, 2, 3, 3, 3, 2}
print(s2)  # {1, 2, 3}

# 面试题：列表去重
# l = [1, 2, 3, 3, 3, 2]
# # 类型转化：将列表转为集合，再将集合转为列表
# # print(set(l))# {1, 2, 3}
# print(list(set(l)))

# (3) 可变类型：列表和字典
# 内置方法：添加和删除
# 添加元素
# s3 = {1, 2, 3}
# # s3.add(4)
# s3.update({3, 4, 5})
# print(s3)

# l = [1, 2, 3]
# l.extend([3, 4, 5])
# print(l)

# 删除元素
s3 = {1, 2, 3}
# ret = s3.remove(2)
# print(ret) # None
# s3.remove(2) # 当删除元素不存在，报错
# s3.discard(2)  # 当删除元素不存在，什么都不发生
# s3.remove(22)
# s3.discard(22)
# s3.pop() # 删除并返回任意集合元素
s3.clear()
print(s3)

# s4 = {1, 2, 3, [4, 5]}
