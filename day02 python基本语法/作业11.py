# 判断用户名密码是否正确

# 预设的正确用户名和密码
correct_username = "admin"
correct_password = "123456"

# 输入用户名和密码
username = input("请输入用户名: ")
password = input("请输入密码: ")

# 判断用户名和密码是否正确
if username == correct_username and password == correct_password:
    print("登录成功！")
else:
    print("用户名或密码错误！")
