# 基于以下数据结构实现一个购物车系统，可以添加商品到购物车，删除商品，打印当前购物车所有商品以及总价
# 改进，从现有库存选择添加
shopping_cart = []

inventory = {
    1: {
        "name": "苹果",
        "price": 122,
        "kuCun": 100
    },
    2: {
        "name": "橘子",
        "price": 32,
        "kunCun": 1000
    },
    3: {
        "name": "香蕉",
        "price": 12,
        "kunCun": 1500
    }
}

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
        print("库存可选商品：")
        print("*" * 40)
        for num, goods in inventory.items():
            print(f"{num}.{goods.get('name'):10}，价格-{goods.get('price'):5} 库存-{goods.get('kunCun'):5}")
        print("*" * 40)

        num = int(input("请输入添加商品的序号："))
        name = inventory[num].get("name")
        price = inventory[num].get("price")
        kunCun = inventory[num].get("kunCun")

        quantity = int(input("请输入添加商品的数量："))

        if quantity>kunCun:
            print("选择数量超过库存！")
        else:
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
