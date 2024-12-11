from decimal import Decimal

x = 1
y = 2
print(1 + 2)

a = 3.14
b = 1.11
print(a + b)
print(a - b)
# ret1 = round(a - b)  # 四舍五入精度限制
# print(ret1)
# ret2 = round(a - b, 2)
# print(ret2)

c = Decimal("3.14")
d = Decimal("1.11")
print(c - d)

# type():打印数据对象的类型名
# x,y,a,b分别是什么类型的数据
print(type(x))
print(type(y))
print(type(a))
print(type(b))
