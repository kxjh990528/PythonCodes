info01 = ["yuan", 23, 189, 75]
print(info01[3])

info02 = {"username": "yuan", "age": 23, "height": 189, "weight": 75}
print(type(info02))  # <class 'dict'>

print(info02["height"])
print(info02["weight"])

# info02["height"] = 192
# print(info02)

del info02["weight"]
print(info02)

info02["email"] = "123@qq.com"
print(info02)
