# 引导用户输入一个双值加法字符串，例如`3+5`或`3 + 5`，计算出两个数字的和，打印出来

# 引导用户输入一个双值加法字符串
expression = input("请输入一个加法表达式（例如：3+5或3 + 5）：")

# 方式一：去除空格并拆分字符串
parts = expression.replace(" ", "").split("+")

# 方式二：直接拆分字符串后面用strip()去除空格，即下面num1num2赋值的时候parts[].strip()再进行类型转化（不过int()会自动处理空格，为了代码严谨加上较好）
# parts =expression.split("+")

# 将拆分后的字符串转换为整数并计算和
if len(parts) == 2:
    if parts[0].isdigit() and parts[1].isdigit():
        num1 = int(parts[0])
        num2 = int(parts[1])
        print(f"{num1} + {num2} = {num1 + num2}")
    else:
        print("输入无效，请确保输入的是数字。")
else:
    print("输入格式不正确，请确保表达式是两个数字的加法。")
