"""
在选座购票中扩写，引导用户输入【普通票/学生票/老年票】，然后分支判断。
print("欢迎来到电影订票系统！")
print("请选择您要进行的操作：")
print("1. 查询电影场次")
print("2. 选座购票")
print("3. 查看订单信息")

choice = int(input("请输入您的选择（1-3）："))

if choice == 1:
    print("正在查询电影场次...")
    # 执行查询电影场次的代码
elif choice == 2:
    print("正在选座购票...")

elif choice == 3:
    print("正在查看订单信息...")
    # 执行查看订单信息的代码
else:
    print("无效的选择！请重新运行程序并输入有效的选项。")
"""
print("欢迎来到电影订票系统！")
print("请选择您要进行的操作：")
print("1. 查询电影场次")
print("2. 选座购票")
print("3. 查看订单信息")

choice = int(input("请输入您的选择（1-3）："))

if choice == 1:
    print("正在查询电影场次...")
    # 执行查询电影场次的代码
elif choice == 2:
    print("正在选座购票...")

    # 引导用户选择票种
    print("请选择票种：")
    print("1. 普通票")
    print("2. 学生票")
    print("3. 老年票")

    ticket_type = int(input("请输入您的选择（1-3）："))

    if ticket_type == 1:
        print("您选择了普通票。")
        # 执行普通票购买流程的代码
    elif ticket_type == 2:
        print("您选择了学生票。")
        # 执行学生票购买流程的代码
    elif ticket_type == 3:
        print("您选择了老年票。")
        # 执行老年票购买流程的代码
    else:
        print("无效的票种选择！请重新选择票种。")

elif choice == 3:
    print("正在查看订单信息...")
    # 执行查看订单信息的代码
else:
    print("无效的选择！请重新运行程序并输入有效的选项。")
