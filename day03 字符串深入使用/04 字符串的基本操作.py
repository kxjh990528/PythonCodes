# (1)字符串不能修改字符值，创建新字符串引用发生变化
# s1 = "yuan"
# s1 = "lin"
# print(s1)
# # s1[0] = "R"
# s1 = "Rain"

# (2)内置函数：len
# s = "hello yuan"
# print(len(s))
# print(s[-1])
# print(s[len(s) - 1])
#
# print(len([1, 2, 3]))
# print(len({"k1": "v1"}))

# (3)拼接
# s1 = "hello"
# s2 = "yuan"
# print(s1 + s2)
# print(s1 + " " + s2)

# name_str = ""
# name1 = "rain"
# name_str += " " + name1
# name2 = "eric"
# name_str += " " + name2
# name3 = "yuan"
# name_str += " " + name3
# name4 = "alvin"
# name_str += " " + name4
# print(name_str)

# print("*" * 25)

# (4) in 返回布尔值
# print("rain" in "rain eric lin")
# print("rai" in "rain eric lin")
# print("rains" in "rain eric lin")
# print("rain" not in "rain eric lin")

# if "rain" in "rain eric lin":  # "rain eric lin"优秀名单
#     print("奖励他")
# else:
#     print("惩罚他")

if "rain" not in "rain eric lin":  # "rain eric lin"黑名单
    print("奖励他")
else:
    print("惩罚他")