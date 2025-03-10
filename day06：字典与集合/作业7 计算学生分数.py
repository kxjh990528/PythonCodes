"""
6. 假设有一个班级的学生成绩数据，数据结构如下：

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 76},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 68},
    {"name": "Eva", "score": 92}
]

请编写程序完成以下操作：
* 计算学生人数。
* 计算班级总分和平均分。
* 找出成绩最高和最低的学生。
"""
# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 76},
#     {"name": "Charlie", "score": 90},
#     {"name": "David", "score": 68},
#     {"name": "Eva", "score": 92}
# ]
#
# # 学生人数
# stu_num = len(students)
# # 总成绩
# score_sum = 0
# # 最高分
# # score_top = 0
# # 下面score_bottom的启发，虽然这里不会造成bug但是为了避免一些特殊值
# score_top = students[0]["score"]
# # 最高分学生
# top_student = {}
# # 最低分 但是0够小，会造成bug，结果是没有学生最低，这样用列表的值进行后续比较可以避免这一错误
# # score_bottom = 0
# score_bottom = students[0]["score"]
# # 最低分学生
# bottom_student = {}
#
# for student in students:
#     # 计算总分
#     score_sum += student["score"]
#
#     # 查找最高分
#     if student["score"] >= score_top:
#         score_top = student["score"]
#         top_student = student
#
#     # 查找最低分
#     if student["score"] <= score_bottom:
#         score_bottom = student["score"]
#         bottom_student = student
#
# print("学生人数：", stu_num)
# print("班级总分：", score_sum)
# # 计算平均分（保留两位）
# # score_avg = round(score_sum / stu_num, 2)
# print(f"班级平均分：{score_sum / stu_num:.2f}")
# print("成绩最高的学生：", top_student)
# print("成绩最低的学生：", bottom_student)

# 课堂讲解
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 76},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 68},
    {"name": "Eva", "score": 92}
]
# 计算学生人数
print(len(students))
# 计算班级总分和平均分
total = 0
for i in students:
    total += i.get("score")

print("total:", total)
print("average:", round(total / len(students), 2))
# 找出成绩最高和最低的学生
max_score = students[0]["score"]
min_score = students[0]["score"]
for studentDict in students:
    score = studentDict.get("score")

    if score > max_score:
        max_score = score

    if score < min_score:
        min_score = score

print("max_score:", max_score)
print("min_score:", min_score)

