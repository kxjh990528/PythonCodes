# (1)upper和lower
# s = "Yuan"
# s2 = s.upper()
# s3=s.lower()
# print(s)
# print(s2)
# print(s3)

# print("Hello World".upper())

# (2)startswith和endswith 返回布尔值
# name = "张三丰"
# print(name.startswith("张"))
# print(name.startswith("张三"))
# print(name.startswith("丰"))
# print(name.endswith("丰"))
# print(name.endswith("三丰"))

# (3)find index查找某子字符串的索引
# s = "hello yuan"
# s.find("yuan")
# print(s.find("yuan"))
# print(s.index("yuan"))
#
# print(s.find("Yuan"))  # 查找不到，返回-1
# print(s.index("Yuan"))  # 查找不到，报错

# (4)strip：去除两段的空格或者换行符
# name = input("姓名：")
# print(name)
#
# ret = name.strip()  # 去除两端的空格或者换行符
# print(ret)
# print(len(ret))

# 案例2
# print("\nyuan\n")
# print("\nyuan\n".strip())

# 案例3
# s = "##abcd#####"
# print(s.strip("#"))
# print(s.lstrip("#"))
# print(s.rstrip("#"))

# (5) isdigit：判断字符串是否为数字字符串
# print("apple".isdigit())
# print("123".isdigit())
# print("123元".isdigit())
# print("123.45".isdigit())

# age_str = input("age:::")
# if age_str.isdigit():
#     age = int(age_str)
#     print(age)
# else:
#     print("非法输入！")

# (6) split() 分割 和 join() 拼接
# cities = "北京 哈尔滨 重庆 大连 武汉"
# ret = cities.split(" ") # ['北京', '哈尔滨', '重庆', '大连', '武汉']
# print(ret)
# print(len(ret))

# 案例1
# ret = ['北京', '哈尔滨', '重庆', '大连', '武汉']
# ret.join(",")
# print(",".join(ret))

# 案例2
# info = "lin|19|185"
# ret = info.split("|")  # ['lin', '19', '185']
# print(ret)
# print(ret[0])
# print(ret[1])
# print(ret[2])

# (7) replace()：子字符串替换
# 案例1
# cities = "北京 哈尔滨 重庆 大连 武汉"
# ret = cities.replace(" ", ",")
# print(ret)

# 案例2
# sentence = "PHP is the best language.PHP...PHP...PHP..."
# ret = sentence.replace("PHP", "JAVA")
# print(ret)

# 案例3
# comments = "这个产品真棒！我非常喜欢。服务很差，不推荐购买。这个餐厅的食物质量太差了，味道不好。我对这次旅行的体验非常满意。这个电影真糟糕，剧情一团糟。这个景点真糟糕，再也不来了！"
# comments = comments.replace("太差了","***").replace("不推荐","***").replace("糟糕","**")
# print(comments)

# (8) count：计算字符串中某个子字符串出现的次数
sentence = "PHP is the best language.PHP...PHP...PHP..."
print(sentence.count("PHP"))  # 4
