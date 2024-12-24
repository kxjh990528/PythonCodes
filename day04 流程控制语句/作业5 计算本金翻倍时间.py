"""
计算初始本金为1万，年利率为0.0325的情况下，需要多少年才能将本金和利息翻倍，即本金和利息的总和达到原来的两倍
"""
import math

# 初始本金和年利率
principal = 10000  # 初始本金
rate = 0.0325  # 年利率

# 目标金额是本金的两倍
# target_amount = 2 * principal
#
# # 使用复利公式求解所需的时间 t
# t = math.log(2) / math.log(1 + rate)
#
# # 输出结果
# print(f"需要 {t:.2f} 年才能将本金翻倍")

# 课堂讲解方法
year = 0
total = principal
while total < 2 * principal:
    total = total + total * rate
    year += 1

print(f"需要 {year} 年才能将本金翻倍")
