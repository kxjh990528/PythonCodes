# 示例：计算BMI并给出健康建议

# 获取用户输入的身高和体重
height = float(input("请输入您的身高（单位：米）："))
weight = float(input("请输入您的体重（单位：千克）："))

# 计算BMI
bmi = weight / (height ** 2)

# 根据BMI给出健康建议
if bmi < 18.5:
    advice = f"您的BMI为 {bmi:.3}，体重过轻，建议增加营养摄入。"
elif 18.5 <= bmi < 24:
    advice = f"您的BMI为 {bmi:.3}，体重正常，继续保持健康的生活方式。"
elif 24 <= bmi < 28:
    advice = f"您的BMI为 {bmi:.3}，体重过重，建议适当控制饮食并增加运动。"
else:
    advice = f"您的BMI为 {bmi:.3}，体重肥胖，建议减少高热量食物摄入并增加运动量。"

# 输出健康建议
print(advice)