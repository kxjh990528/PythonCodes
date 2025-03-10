from http.cookiejar import offset_from_tz_string
from tkinter.font import names

gf = {"name": "高圆圆", "age": 32}

# （1）增或改：字典对象.update(字典对象)
# ret = gf.update({"age": 27})
# print(ret)
# print(gf)

# 添加一个键值
# gf.update({"height": 175})
# print(gf)
# temp_dict = {"age": 27, "height": 175}
# gf.update(temp_dict)
# print(gf)

# （2）删除键值对 pop()
# del gf("age")
# l = [1, 2, 3]
# ret = l.pop(2)
# print(ret)
# print(l)
# ret = gf.pop("age")
# print(ret)

# （3）查看键值 get()
# print(gf["names"])
# name = gf.get("name")
# print(name)
#
# age = gf.get("ages") # 当键不存在，默认返回None
# print(age)
#
# if age:
#     print(age)
# else:
#     print("没有获取到！")

# 案例
# name = gf.get("name")
# if name:
#     print(name)
# else:
#     print("匿名用户")      

name = gf.get("name", "匿名用户")
print(name)

name = gf.get("names", "匿名用户")
print(name)

