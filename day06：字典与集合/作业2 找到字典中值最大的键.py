# 给定一个字典，找到字典中值最大的键
my_dict = {'A': 10, 'B': 5, 'C': 15, 'D': 20}

# 方法一 遍历
max_key = None
max_val = 0

for key, val in my_dict.items():
    if val > max_val:
        max_val = val
        max_key = key

print(max_key)

# 方法二 使用 max() 函数找出值最大的键
max_key = max(my_dict, key=my_dict.get)
print(max_key)