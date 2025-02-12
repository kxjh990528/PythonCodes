gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']

# (1)成员判断
# print("yuan" in "rain yuan eric")
# print("yuans" in "rain yuan eric")
# print("yuan" in "rain yuans eric")

# name_list = ["rain", "eric", "alvin", "yuan"]
# print("yuan" in name_list)
# print("yuans" in name_list)

# name_list = ["rain", "eric", "alvin", "yuans"]
# print("yuan" in name_list)
# print("yuans" in name_list)

# l = [1, 2, 3, 4, 5]
# print(1 in l)
# print("1" in l)

# (2) 拼接+
# s1 = "hello"
# s2 = " yuan"
# print(s1 + s2)
#
# l1 = [1, 2, 3]
# # l2 = [4, 5, 6]
# l2 = [6, 5, 4]
# print(l1 + l2)
# print(l1)
# print(l2)

# (3) 列表循环：列表作为一个容器对象，可以通过for循环进行遍历
# 字符串，列表可以for循环

# name_list = ["张三", '李四', "王五"]
name_list = ["rain", "eric", "alvin", "yuan", "Alex"]

# for name in name_list:
#     # print(name)
#     # print(name.upper())
#     if name.startswith("a"):
#         print(name)

# for name in name_list:
#     print(name)
#     print(name.upper())
#     方式一
#     if name.startswith("a") or name.startswith("A"):
#         print(name)
#     方式二
#     if name.upper().startswith("A"):
#         print(name)

# s = "  yuan  "
# print(s.strip().capitalize().isdigit())

# (4)计算列表的元素个数：len
print(len("hello yuan!"))
print(len([1, 2, 3, 4, 5, 6]))
print(len(["rain", "eric", "alvin", "yuan", "Alex"]))
print(len({"k1": "v1", "k2": "v2"}))
