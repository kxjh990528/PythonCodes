shopping_cart = []

while True:
    print("--- 购物车清单 ---")
    print("1. 添加商品")
    print("2. 删除商品")
    print("3. 查看购物车")
    print("4. 结束程序")

    choice = input("请输入选项：")

    if choice == "1":
        item = input("请输入要添加的商品：")
        shopping_cart.append(item)
        print("已添加商品:", item)
        print()

    elif choice == "2":
        if len(shopping_cart) == 0:
            print("购物车为空，无法删除商品。")
        else:
            item = input("请输入要删除的商品：")
            if item in shopping_cart:
                shopping_cart.remove(item)
                print("已删除商品:", item)
            else:
                print("购物车中没有该商品。")
        print()

    elif choice == "3":
        if len(shopping_cart) == 0:
            print("购物车为空。")
        else:
            print("*" * 15)
            print("购物车内容:")
            for item in shopping_cart:

                print(item)
            print("*" * 15)
        print()

    elif choice == "4":
        print("程序已结束。")
        break

    else:
        print("无效选项，请重新输入。")
        print()