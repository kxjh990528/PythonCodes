# 对列表元素先去重再排序：`l = [1, 12, 1, 2, 2, 3, 5]`
l = [1, 12, 1, 2, 2, 3, 5]

# 先转化成集合去重，再转化为列表,reverse=False默认升序，可不写
print(sorted(list(set(l)), reverse=False))

# 课堂讲解
# print(list(set(l)))
new_l = list(set(l))
new_l.sort(reverse=True)
print(new_l)
