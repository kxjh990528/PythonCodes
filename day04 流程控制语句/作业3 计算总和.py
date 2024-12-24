"""
计算1-2+3-4+......-1000最终的结果,能整除13的数不参与计算
"""

# 总和初始化
total_sum = 0

# 方法一
# 计算 1 到 1000 中能被 13 整除的数
# for i in range(1, 1001):
#     if i % 13 != 0:  # 排除能被 13 整除的数
#         if i % 2 == 1:  # 奇数位置，加上 i
#             total_sum += i
#         else:  # 偶数位置，减去 i
#             total_sum -= i


# print("最终的计算结果是：", total_sum)

# 方法二
for i in range(1, 1001):
    if i % 13 == 0:  # 跳过能被十三整除的情况
        continue
    else:
        if i % 2 == 1:  # 奇数位置，加上
            total_sum += i
        else:  # 偶数位置，减去 i
            total_sum -= i

print("最终的计算结果是：", total_sum)
