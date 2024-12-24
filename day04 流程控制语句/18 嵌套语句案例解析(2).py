import random

name = "勇士"
health = 100
coins = 0
exp = 0

print("欢迎来到地下城！")

while 1:
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


