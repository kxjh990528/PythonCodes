# 案例1
# 语文成绩大于100分同时（并且）数学成绩大于100分
# chinese = 140
# math = 98

# 与运算 and
# 真与真 结果为真
# 真与假 结果为假
# 假与真 结果为假
# 假与假 结果为假
# ret = chinese > 100 and math > 100
# print(ret)
#
# if chinese > 100 and math > 100:
#     print("买礼物")
# else:
#     print("小惩罚")

# 案例2
# 语文成绩大于100分或数学成绩大于100分
# chinese = 140
# math = 25
# # 或运算:or
# # 真或真 结果为真
# # 真或假 结果为真
# # 假或真 结果为真
# # 假或假 结果为假
# ret = chinese > 100 or math > 100
# print(ret)
#
# if chinese > 100 or math > 100:
#     print("买礼物")
# else:
#     print("小惩罚")

# 逻辑运算符
# print(not 3 > 2)
# print(not 3 == 2)

# 案例3：
# 用户输入一个年龄，判断是否符合20-35之间的要求
# age = int(input("年龄"))
#
# # if age > 20 and age < 35:
# if 20 < age < 35:
#     print("符合要求")
# else:
#     print("不符合要求")

# 成员运算符：in
print("rain" in "lin rain heavy eric")
print("rai" in "lin rain heavy eric")
print("rains" in "lin rain heavy eric")
print("rains al" in "lin rain heavy eric")
print("lin" in ["123", "lin", "真假"])
