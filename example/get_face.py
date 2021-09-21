# -*-coding:utf8-*-

import urllib.request
import re

f = open("bilibili_user_face.txt")
line = f.readline()

for i in range(1, 100):
    if re.match('http://i0.*', line):
        line = f.readline()
        #print('noface:' + str(i))
    else:
        path = r"D://Python/bilibili-user-master/user_face/" + str(i) + ".jpg"
        data = urllib.request.urlretrieve(line, path)
        line = f.readline()
        print('succeed:' + str(i)+'\n'+line)

f.close()
