# 案例1：函数返回空值
ret = print("hello")
print(ret, type(ret))  # None <class 'NoneType'>

# 案例2：初始化赋值
# 模拟计算过程
num1 = int(input("请输入num1："))
num2 = int(input("请输入num2:"))
operator = input("请输入运算符：")
result = None
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("非法操作")

print(result)
