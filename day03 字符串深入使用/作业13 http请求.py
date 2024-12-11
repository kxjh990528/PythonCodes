# HTTP协议格式数据组装，引导用户分别输入请求方式，请求URL以及若干个请求头
# 请输入 HTTP 请求方法：GET
# 请输入 URL：https://www.example.com/api/data
# 请输入 HTTP 协议：HTTP/1.1
# 请输入请求头信息（键值对用冒号分隔，多个键值对用逗号分隔）：User-Agent: MyClient/1.0,Authorization: Token abcdef123456

# 引导用户输入信息
method = input('请输入 HTTP 请求方法：')
url = input('请输入 URL：')
proto_name = input('请输入 HTTP 协议：')
headers = input('请输入请求头信息（键值对用冒号分隔，多个键值对用逗号分隔）:')

# 获取路径
path = url.split('com')[-1]
# 拼接第一行
first_line = method + ' ' + path + '' + proto_name
# print('first_line:' + first_line)

# 将头信息分隔后，再用'\n'连接（join()），然后把第一行一起打印
print(first_line + '\n' + '\n'.join(headers.split(',')))

