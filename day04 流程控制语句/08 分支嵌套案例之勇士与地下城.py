"""
 勇士与地下城的场景续写：
（1）怪物房： 遇到了史莱姆
                1. 选择攻击，战胜史莱姆，则经验加20，金币加20，失败则经验减20，金币减20，血值减20，成功的概率为50%。
                2. 选择逃跑，则金币减20
 (2) 宝箱房: 你打开了宝箱，获得了钥匙
 (3) 陷阱房: 你触发了陷阱，受到了毒箭的伤害,血值减10
 (4) 商店:   你来到了商店，打印当前血值和金币，一个金币买一个药水对应10个血值，引导是否购买药水
                1. 购买，引导购买几个金币的药水，并完成减金币和增血值
                2. 不购买，打印退出商店

"""

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
    action = input("请选择行动：(1)攻击  (2)逃跑")
    if action == "1":
        attack = random.randint(1, 20)
        if attack >= 10:
            print("你击败了史莱姆")
            coins += 10
        else:
            print("你的攻击没有命中！")
            health -= 20
    elif action == "2":
        print("你逃跑了，但失去了一些生命值")
        health -= 10
    else:
        print("无效的选择！请重新选择。")

elif room == "宝箱房":
    print("你打开了宝箱，获得了钥匙")

elif room == "陷阱房":
    print("你触发了陷阱，受到了毒箭的伤害")
    health -= 10
elif room == "商店":

    choice = input("你来到了商店，购买了药水，是否购买？【Y/N】")
    if choice == "Y" and coins >= 5:
        print("购买药水成功")
        coins -= 5
        health += 20
    else:
        print("退出商店")

print(f"""
    当前生命值：{health}
    当前经验值：{exp}
    当前金币：{coins}
    """)
