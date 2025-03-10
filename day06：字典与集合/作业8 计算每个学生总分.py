"""
8. 假设有一个嵌套字典，表示学生的成绩数据，数据结构如下：
students = {
    "Alice": {"math": 85, "english": 90, "history": 78},
    "Bob": {"math": 76, "english": 82, "history": 88},
    "Charlie": {"math": 90, "english": 92, "history": 86},
    "David": {"math": 68, "english": 72, "history": 80},
    "Eva": {"math": 92, "english": 88, "history": 90}
}
请编写程序完成以下操作：
* 打印每个学生的姓名和总分。
* 打印每个学生的平均分。
"""
students = {
    "Alice": {"math": 85, "english": 90, "history": 78},
    "Bob": {"math": 76, "english": 82, "history": 88},
    "Charlie": {"math": 90, "english": 92, "history": 86},
    "David": {"math": 68, "english": 72, "history": 80},
    "Eva": {"math": 92, "english": 88, "history": 90}
}

for key, val in students.items():
    print(f"学生：{key:<10}，总分：{sum(val.values()):<5}，平均分：{sum(val.values()) / len(val):<.2f}")

# 课堂代码
for name, stu_socre_dict in students.items():
    # print(name, stu_socre_dict)
    total = 0
    for sub_score in stu_socre_dict.values():
        total += sub_score
    print(name, total, round((total / len(stu_socre_dict) / 2)))
