"""
实现一个简单的 todo_list（待办事项列表）功能，实现添加，删除，置顶和完成的代办事项。
"""

todo_list = [
    # ["学习python", False]
]

while True:
    print("========== ToDo List ==========")
    print("1. 添加代办事项")
    print("2. 删除代办事项")
    print("3. 置顶代办事项")
    print("4. 完成代办事项")
    print("5. 退出")

    # 引导用户输入
    choice = input("请输入您的选择：")

    if choice == "1":
        # 添加待办事项
        title = input("请输入添加的待办事项：")
        item = [title, False]
        todo_list.append(item)
        print(f"待办事项{title}添加成功")

    elif choice == "2":
        if len(todo_list) == 0:
            print("目前没有待办事项")
        else:
            # 删除待办事项
            num = int(input("请输入要删除的待办事项的序号："))
            index = num - 1

            if index < 0 or index > len(todo_list):
                print("索引无效")
            else:
                index = num - 1
                del_item = todo_list.pop(index)
                print(f"{del_item[0]}删除成功！")

    elif choice == "3":
        if len(todo_list) == 0:
            print("目前没有待办事项")
        else:
            # 置顶待办事项
            num = int(input("请输入要置顶的待办事项的序号："))
            index = num - 1

            if index < 0 or index > len(todo_list):
                print("索引无效")
            else:
                up_item = todo_list.pop(index)
                todo_list.insert(0, up_item)
                print(f"{up_item}置顶成功！")

    elif choice == "4":
        if len(todo_list) == 0:
            print("目前没有待办事项")
        else:
            if len(todo_list) < 2:
                print("目前没有足够的待办事项置顶")
            else:
                # 完成待办事项
                num = int(input("请输入要置顶的待办事项的序号："))
                index = num - 1

                if index < 0 or index > len(todo_list):
                    print("索引无效")
                else:
                    todo_list[index][1] = True
                    print(f"{todo_list[index][0]}已完成，设置成功！")

    elif choice == "5":
        break

    else:
        print("无效输入")

    print("==========当前待办事项==========")

    for i, todo in enumerate(todo_list, 1):
        flag = todo[1]
        state = None
        if flag:
            state = "已完成"
        else:
            state = "未完成"
        print(f"{i}. {todo[0]},{todo[1]}")
