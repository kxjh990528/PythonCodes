import random

# 生成300名员工，员工编号为1到300
staff = list(range(1, 301))

# 一等奖人数
first_prize_count = 3
# 二等奖人数
second_prize_count = 6
# 三等奖人数
third_prize_count = 30


# 奖项设置
first_winner = []
second_winner = []
third_winner = []

# 抽一等奖
for first in range(first_prize_count):
    winner = random.choice(staff)
    first_winner.append(winner)
    staff.remove(winner)

# 抽二等奖
for second in range(second_prize_count):
    winner = random.choice(staff)
    second_winner.append(winner)
    staff.remove(winner)

# 抽三等奖
for third in range(third_prize_count):
    winner = random.choice(staff)
    third_winner.append(winner)
    staff.remove(winner)


# 打印结果
print("一等奖：泰国5日游+手术费报销的员工编号：", first_winner)
print("二等奖：iPhone16手机的员工编号：", second_winner)
print("三等奖：3斤苹果的员工编号：", third_winner)

