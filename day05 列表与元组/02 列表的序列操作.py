# gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']

# 一、索引操作
# (1)查看元素：列表对象[索引]，获取元素，获取的只有一个元素值

# print(gf_name_list[2])
# print(gf_name_list[4])
# print(gf_name_list[-1])

# (2) 修改元素
# gf_name_list[3] = "佟丽娅"
# print(gf_name_list)

# 二、切片操作
# (1)查看多个元素：列表对象[开始索引:结束索引:步长=1(默认)], 获取多个值的子列表

# print("hello"[1:4])  # 子字符串
# print(gf_name_list[1:])  # 子列表
# print(gf_name_list[0:3])
# print(gf_name_list[:3])  # 缺省0
# print(gf_name_list[2:5])
# print(gf_name_list[2:])  # 缺省最后一个值
# print(gf_name_list[:])
# print(gf_name_list[-3:-1])
# print(gf_name_list[-3:])

# 步长=1
# 步长是正数：从小向大切（从左向右切）
# 步长是负数：从大向小切（从右向左切）
# print(gf_name_list[1:4])
# print(gf_name_list[4:1])
# print(gf_name_list[4:1:-1])
# print(gf_name_list[-4:-2])
# print(gf_name_list[-2:-4:-1])
# print(gf_name_list[::1])
# print(gf_name_list[::2])
# print(gf_name_list[::3])
# print(gf_name_list[::-1])
# print(gf_name_list[::-2])

# (2)修改多个元素：
gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']

# gf_name_list[1:4] = 100, 200, 300
# gf_name_list[1:4] = [100, 200, 300]
# gf_name_list[1:4] = ['霹雳狐', '小允', '小苏菲']
# print(gf_name_list)

# 面试题
s = "hello yuan"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# s[-2] = 'A'
ret = list(s)
print(ret)
ret[-2] = 'A'
print(ret)
ret2 = "".join(ret)
print(ret2)
