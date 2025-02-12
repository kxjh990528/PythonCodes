# l = ["yuan 18 185cm", "rain 23 175cm"]

# 初始化客户信息列表
customers = [
    ["Alice", 25, "alice@example.com"],
    ["Bob", 30, "bob@example.com"],
    ["Charlie", 35, "charlie@example.com"]
]

while 1:
    # 功能整合
    print("""
           1. 添加客户
           2. 删除客户
           3. 修改客户
           4. 查询一个客户
           5. 查询所有客户
           6. 退出
    
        """)

    choice = input("请输入您的选择：")

    if choice == "1":
        # (1)添加客户 append

        name = input("请输入客户的姓名：")
        age = input("请输入添加客户的年龄：")
        email = input("请输入添加客户的邮箱：")

        # customers.append([name, age, email])

        new_customer = [name, age, email]
        customers.append(new_customer)

        print(f"添加客户{name}成功!")
        # print("当前客户列表：", customers)
    elif choice == "2":
        # (2)删除客户

        del_customer_name = input("请输入删除客户的姓名：")

        flag = False

        for customerL in customers:
            # print(customerL)
            if customerL[0] == del_customer_name:
                customers.remove(customerL)
                print(f"客户{del_customer_name}删除成功！")
                flag = True
                break

        if flag:
            print("当前客户列表：", customers)
        else:
            print(f"客户{del_customer_name}不存在！")

    elif choice == "3":
        # (3)修改客户

        update_customer_name = input("请输入修改客户的姓名：")

        name = input("请输入新的客户的姓名：")
        age = input("请输入修改客户的年龄：")
        email = input("请输入修改客户的邮箱：")

        for customersL in customers:
            if customersL[0] == update_customer_name:
                customersL[0] = name
                customersL[1] = age
                customersL[2] = email
                break

        # print("当前客户列表：", customers)

    elif choice == "4":
        # (4)查看某一个客户

        query_customer_name = input("请输入查看客户的姓名：")

        for customersL in customers:
            if customersL[0] == query_customer_name:
                print(f"姓名：{customersL[0]}，年龄：{customersL[1]}，邮箱：{customersL[2]}")
                break

    elif choice == "5":
        # (5)遍历每一个客户信息
        # if len(customers) == 0:
        #     print("当前没有任何客户信息")
        # else:
        #     for customersL in customers:
        #         print(f"姓名：{customersL[0]:10}，年龄：{customersL[1]}，邮箱：{customersL[2]}")
        if customers:
            for customersL in customers:
                print(f"姓名：{customersL[0]:10}，年龄：{customersL[1]}，邮箱：{customersL[2]}")
        else:
            print("当前没有任何客户信息")

    elif choice == "6":
        print("退出程序!")
        break
    else:
        print("输入内容格式不对！")
