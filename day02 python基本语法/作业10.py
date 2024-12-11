# 输入一个数字，判断是否是三位数且能被13整除
num = int(input("请输入一个数字："))

if 100 <= num <= 999 and num % 13 == 0:
    print(f"{num} 是三位数且能被13整除")
else:
    print(f"{num} 不是三位数且不能被13整除")