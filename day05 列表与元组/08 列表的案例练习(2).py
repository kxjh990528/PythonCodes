# 案例2：扑克牌发牌
import random

# 版本1
# poke_types = ['♥', '♦', '♠', '♣']
# poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

# 版本2
poke_types = '♥♦♠♣'
poke_nums = '2345678910JQKA'
poke_list = []
for p_type in poke_types:
    for p_num in poke_nums:
        # print(f"{p_type}{p_num}")
        poke_list.append(f"{p_type}{p_num}")

print(poke_list)
