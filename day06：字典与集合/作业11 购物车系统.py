# 基于以下数据结构实现一个购物车系统，可以添加商品到购物车，删除商品，打印当前购物车所有商品以及总价
shopping_cart = [
    {
        "name": "mac电脑",
        "price": 14999,
        "quantity": 1
    },
    {
        "name": "iphone15",
        "price": 9980,
        "quantity": 1
    }
]

while 1:
    # 功能整合
    print("""
        请选择操作：
           1. 添加商品
           2. 删除商品
           3. 打印购物车所有商品以及总价
           4. 退出
        """)

    choice = input("请输入您的选择：")

    # 添加商品
    if choice == "1":
        add_good_name = input("请输入商品名称：")
        add_good_price = int(input("请输入商品价格："))
        add_good_quantity = int(input("请输入商品数量："))
        shopping_cart.append({"name": add_good_name, "price": add_good_price, "quantity": add_good_quantity})
        print(f"添商品{add_good_name}成功!")

    # 删除商品
    elif choice == "2":
        del_good_name = input("请输入要删除的商品名称：")

        flag = False

        for good in shopping_cart:
            if good.get("name") == del_good_name:
                shopping_cart.remove(good)
                print(f"商品{del_good_name}删除成功！")
                flag = True
                break

    # 打印购物车所有商品以及总价
    elif choice == "3":
        for good in shopping_cart:
            total_price = good.get("price") * good.get("quantity")
            print(f"商品名称：{good.get('name'):10}，总价：{total_price:<}")

    elif choice == "4":
        print("退出程序!")
        break
    else:
        print("输入内容格式不对！")

# 课堂讲解
while 1:
    # 功能整合
    print("""
        请选择操作：
           1. 添加商品
           2. 删除商品
           3. 打印购物车
           4. 退出
        """)

    choice = input("请输入您的选择：")

    # 添加商品
    if choice == "1":
        name = input("请输入商品名称：")
        price = float(input("请输入商品价格："))
        quantity = int(input("请输入商品数量："))

        shopping_cart.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print("添加商品成功", shopping_cart)

    # 删除商品
    elif choice == "2":
        num = int(input("请输入删除商品的序号："))
        index = num - 1
        del_goods = shopping_cart.pop(index)
        print(f"商品{del_goods.get('name')}删除成功！")

    # 打印购物车
    elif choice == "3":
        print("当前购物车展示：")
        print("-" * 40)
        total = 0
        for i, goods in enumerate(shopping_cart):
            name = goods.get("name")
            price = goods.get("price")
            quantity = goods.get("quantity")

            print(f"{i}.{name:10}，价格-{price:5} 数量-{quantity:5}")
            total += price * quantity
        print("-" * 40)
        print("总值：", total)

    elif choice == "4":
        print("感谢使用购物车")
        break

    else:
        print("无效输入，请重新选择！")
