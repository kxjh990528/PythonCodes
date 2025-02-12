# 引导用户输入页数（每页获取3条数据），实现对作品列表的切片获取,并进行格式化打印

# 假设您有一个作品列表
works = ["作品1", "作品2", "作品3", "作品4", "作品5", "作品6", "作品7", "作品8", "作品9", "作品10", "作品11", "作品12",
         "作品13"]

# 用户输入1则获取：["作品1", "作品2", "作品3"]    page=1  [0:3]
# 用户输入2则获取：["作品4", "作品5", "作品6"]    page=2  [3:6]
# 用户输入3则获取：["作品7", "作品8", "作品9"]    page=3  [6:9]
# 用户输入4则获取：["作品10", "作品11", "作品12"] page=4  [9:12]

# 引导用户输入页数
page = input("请输入页数：")

# 判断输入是否为数字
if page.isdigit():
    page = int(page)

    # 每页获取3条数据
    if page < 1:
        print("页数不能小于1！")
    else:
        start_index = (page - 1) * 3  # 计算起始索引
        end_index = start_index + 3  # 计算结束索引

        # 如果用户输入的页数超出了作品列表的范围
        if start_index >= len(works):
            print("输入的页数超出了可用范围！")
        else:
            # 获取当前页的作品
            current_page_works = works[start_index:end_index]

            # 格式化打印结果
            print(f"第{page}页的作品列表: {current_page_works}")
else:
    print("请输入一个有效的数字页数！")

per_page_num = 3

while 1:
    page_num = int(input("请输入查询的页数："))

    # 分页
    total_page, b = divmod(len(works), per_page_num)
    if b != 0:
        total_page += 1

    if page_num > total_page:
        print("已经超过最大页数！")

    start_index = (page_num - 1) * per_page_num
    end_index = start_index + per_page_num

    work_list = works[start_index:end_index]

    for work in work_list:
        print(work)
