# 编写一个Python程序，输入一个三位数。将其拆分为百位数，十位数和个位数，井输出它们的和

# 引导用户输入一个三位数
number = input("请输入一个三位数：")

# 确保输入的是一个三位数
if len(number) == 3 and number.isdigit():
    # 拆分百位、十位和个位
    hundred = int(number[0])
    ten = int(number[1])
    one = int(number[2])

    # 计算它们的和
    sum_digits = hundred + ten + one

    # 输出结果
    print(f"百位数：{hundred}, 十位数：{ten}, 个位数：{one}")
    print(f"它们的和是：{sum_digits}")
else:
    print("请输入一个有效的三位数。")