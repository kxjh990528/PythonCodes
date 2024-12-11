# 将`Unix/Linux`系统下的路径字符串`"/Users/yuan/npm/index.js"`转换
# 为`Windows`系统下的路径字符串`"\Users\yuan\npm\index.js"`。请使用两种方式来实现路径转换

# Linux盘符路径
linux_path = '/Users/yuan/npm/index.js'

# 第一种方法：直接用replace()函数
windows_path1 = linux_path.replace("/", "\\")
print(windows_path1)

# 第二种方法：拆分重组
# windows_path2 = ''
# path_parts = linux_path.lstrip('/').split('/')
# for path in path_parts:
#     windows_path2 += ('\\' + path)
# print(windows_path2)
windows_path2 = linux_path.split('/')
print('\\'.join(windows_path2))