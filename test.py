import datetime
import hashlib
import time

s = ""

for i in range(1000000):
    s += hashlib.sha512(str(time.time()).encode()).hexdigest()
    print(i)

with open("./3gb_file.txt", 'w') as f:
    f.write(s)