#  场景：
# （1）怪物房： 遇到了史莱姆，并打败了它，金币加5，经验加10！
#  (2) 宝箱房: 你打开了宝箱，获得了钥匙
#  (3) 陷阱房: 你触发了陷阱，受到了毒箭的伤害,血值减10
#  (4) 商店:   你来到了商店，购买了药水,金币减5，血值加20


import random

name = "勇士"
health = 100
coins = 0
exp = 0

print("欢迎来到地下城！")

print(f"""
    当前生命值：{health}
    当前经验值：{exp}                                            
    当前金币：{coins}
    """)

input("按下 Enter 进入下一个房间...")
room = random.choice(["怪物房", "宝箱房", "陷阱房", "商店"])

if room == "怪物房":
    print("你遇到了史莱姆，并打败了它")
    exp += 10
    coins += 5
    print("金币加5，经验加10！")

elif room == "宝箱房":
    print("你打开了宝箱，获得了钥匙")

elif room == "陷阱房":
    print("你触发了陷阱，受到了毒箭的伤害")
    health -= 10
elif room == "商店":

    print("你来到了商店，购买了药水")
    coins -= 5
    health += 20

print(f"""
    当前生命值：{health}
    当前经验值：{exp}
    当前金币：{coins}
    """)