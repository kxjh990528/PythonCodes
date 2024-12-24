"""
1.首先，程序使用random.randint函数产生一个1~10之间的随机数。
2.然后，程序通过for循环提示玩家输入一个猜测的数字，玩家可以输入一个1~10之间的整数。
3.如果玩家猜对了数字，程序输出恭喜玩家的信息并结束游戏；如果玩家猜错了，程序会根据玩家输入的数字与随机数之间的大小关系来提示玩家是否猜对，并在每次猜错后告诉玩家还剩下几次机会。
4.如果玩家在三次机会内猜对了数字，程序输出恭喜玩家的信息并结束游戏；否则程序输出很遗憾的信息并结束游戏。
"""
# import random
#
# # 生成一个随机数
# ran_num = random.randint(1, 10)
# chances = 3
#
# print("欢迎来到猜数字游戏！")
# print("我已经想好了一个1到10之间的数字。你有三次机会猜对它。")
#
# for i in range(chances):  # 控制最多3次机会
#     guess = int(input(f"第 {i + 1} 次猜测：请输入一个1到10之间的整数："))
#     if guess == ran_num:
#         print("恭喜玩家！")
#         break  # 猜对了，直接结束游戏
#     elif guess != ran_num:
#         if guess < ran_num:
#             print("猜小了！")
#         elif guess > ran_num:
#             print("猜大了！")
#     # 提示还剩余的机会
#     if i < chances - 1:
#         print(f"你还有 {chances - i - 1} 次机会。")
# else:
#     print("游戏结束，很遗憾您没有猜对！")

# 课堂讲解代码
import random

# 案例一：
# secret_num = random.randint(1, 10)
#
# for i in range(3):
#     guess_num = int(input("请输入一个数字，范围【1-10】:"))
#
#     # 判断
#     if guess_num > secret_num:
#         print("猜大了")
#     elif guess_num < secret_num:
#         print("猜小了")
#     else:
#         print("恭喜您，猜对了，数字正是", guess_num)
#         break
#
# else:
#     print("很遗憾三次机会已经用完")

# 案例二：
secret_num = random.randint(1, 10)
max_guesses = 3

for i in range(1, max_guesses + 1):
    guess_num = int(input("请输入一个数字，范围【1-10】:"))

    # 判断
    if guess_num > secret_num:
        print("猜大了")
    elif guess_num < secret_num:
        print("猜小了")
    else:
        print("恭喜您，猜对了，数字正是", guess_num)
        break

    # 提示
    remaining_guesses = max_guesses - i
    if remaining_guesses > 0:
        print(f"您还剩下{remaining_guesses}次机会，请珍惜！")
    else:
        print("很遗憾三次机会已经用完")

# else:
#     print("很遗憾三次机会已经用完")
