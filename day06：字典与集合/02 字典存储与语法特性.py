# 字典
# info_dict = {"username": "yuan", "age": 23, "height": 189, "weight": 75}

# print((hash("apple")))
# print(bin(4)) # 十进制转换二进制
# print(bin(5)) # 十进制转换二进制
# print(bin(6)) # 十进制转换二进制
# print(bin(hash("apple")))
#
# print(bin(hash("name")))
# print(bin(hash("age")))
# print(bin(hash("height")))

# 键的要求
# {[]: "123"}  # TypeError: unhashable type: 'list'
# {{}: "123"}  # TypeError: unhashable type: 'dict'

# {(1, 2, 3): 100}
# # {True: 100}
# #
# # {"": "yuan"}
# # {1001: "yuan"}

# 补充：3.7+版本 默认有序字典
info_dict = {"username": "yuan", "age": 23, "height": 189, "weight": 75}
print(info_dict)
