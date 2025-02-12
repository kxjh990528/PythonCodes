"""
给定一个嵌套列表，表示学生的成绩数据，数据结构如下：
scores = [[85, 90, 78], [76, 82, 88], [90, 92, 86], [68, 72, 80], [92, 88, 90]]

请编写程序完成以下操作：
* 计算每个学生的平均分。
* 计算每科的平均分。
"""

# 定义学生成绩数据
scores = [[85, 90, 78], [76, 82, 88], [90, 92, 86], [68, 72, 80], [92, 88, 90]]

# 计算每个学生的平均分
student_averages = []
for student_scores in scores:
    avg_score = sum(student_scores) / len(student_scores)
    student_averages.append(avg_score)

# 计算每科的平均分
subject_averages = []
num_subjects = len(scores[0])
for i in range(num_subjects):
    subject_scores = [student_scores[i] for student_scores in scores]
    avg_score = sum(subject_scores) / len(subject_scores)
    subject_averages.append(avg_score)

# 输出结果
print("每个学生的平均分:", student_averages)
print("每科的平均分:", subject_averages)

# 计算每个学生的平均分
# stu_average_list = []
#
# for stu_score_list in scores:
#     stu_total = 0
#     for stu_subject_score in stu_score_list:
#         stu_total += stu_subject_score
#
#     stu_average = round(stu_total / len(stu_score_list), 2)
#     stu_average_list.append(stu_average)
#
# # 计算每科平均分
# subject_average_list = []
# subject_num = 3
#
# for i in range(subject_num):
#     stu_total = 0
#     for stu_score_list in scores:
#         stu_total += stu_score_list[i]

