# 字典值的乘积：编写一个程序，计算给定字典中所有值的乘积：`my_dict = {'A': 2, 'B': 3, 'C': 4, 'D': 5}`
my_dict = {'A': 2, 'B': 3, 'C': 4, 'D': 5}

# 初始化乘积为 1
product = 1

# 遍历字典中的值并计算乘积
for value in my_dict.values():
    product *= value

print(product)

