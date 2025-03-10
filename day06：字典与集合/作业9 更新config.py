# 配置字典中的查询操作：更新config中服务器的端口为`8090`，日志级别更新为`DEBUG`
config = {
    "数据库": {
        "主机": "localhost",
        "端口": 3306,
        "用户名": "admin",
        "密码": "password"
    },
    "服务器": {
        "IP地址": "192.168.0.1",
        "端口": 8080,
        "日志级别": "INFO"
    },
    # ...
}

config["服务器"].update({"端口": 8090, "日志级别": "DEBUG"})
print(config)

# 课堂讲解
config["服务器"]["端口"] = 8090
config["服务器"]["日志级别"] = "DEBUG"
print(config)
