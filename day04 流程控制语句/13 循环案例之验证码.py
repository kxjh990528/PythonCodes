"""

# 假设有一个变量s的初始值为""，将s拼接5次，每次增加值分别为"A"，"B"，"C"，然后打印s的值。
s = ""
s += "A"
s += "B"
s += "C"
print(s)

"""

import random
import string

char = string.ascii_letters + string.digits

count = 0
randomCodes = ""
while count < 10:
    code = random.choice(char)
    randomCodes += code
    count += 1

print(randomCodes)
