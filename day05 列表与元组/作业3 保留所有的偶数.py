# l=[23,4,5,66,76,12,88,23,65],l保留所有的偶数
l = [23, 4, 5, 66, 76, 12, 88, 23, 65]

# 方法一：遍历元素
# 不可以用remove，remove后的索引会改变会造成错误！如果要用remove可浅拷贝一下
# l2 = []
# for i in l:
#   if i % 2 != 0:
#       l.remove(i)
#   if i % 2 == 0:
#       l2.append(i)

# l2 = []
# 浅拷贝一层，没关系了
# for i in l[:]:
#   if i % 2 != 0:
#       l.remove(i)
#   if i % 2 == 0:
#       l2.append(i)

# print(l)
# print(l2)

# 方法二：列表推导式
even_numbers = [i for i in l if i % 2 == 0]

print(even_numbers)
