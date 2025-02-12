#  案例1：构建一个列表，存储1-10的平方值

# l = []
# for i in range(1, 11):
#     # print(i ** 2)
#     l.append(i ** 2)

# print(l)

# 构建一个列表，存储1-10的偶数平方值

# l = []
# for i in range(1, 11):
#     # print(i ** 2)
#     l.append(i ** 2)
#
# print(l)

# 案例2：扑克牌发牌
import random

poke_types = ['♥️', '♦️', '♠️', '♣️']
poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
poke_list = []
for p_type in poke_types:
    for p_num in poke_nums:
        # print(f"{p_type}{p_num}")
        poke_list.append(f"{p_type}{p_num}")

print(poke_list)

# (1) 抽王八
# random.choice()：多选一
# ret1 = random.choice(poke_list)
# print(ret1)
# ret2 = random.choice(poke_list)
# print(ret2)
# ret3 = random.choice(poke_list)
# print(ret3)

# (2) 炸金花
# random.sample: 多选多
ret1 = random.sample(poke_list, 3)

print(ret1)

for i in ret1:
    poke_list.remove(i)

print(len(poke_list))

ret2 = random.sample(poke_list, 3)
for i in ret2:
    poke_list.remove(i)

print(len(poke_list))

ret3 = random.sample(poke_list, 3)
print(ret1)
print(ret2)
print(ret3)
