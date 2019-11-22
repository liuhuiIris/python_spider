#coding:utf8
import urllib2
import cookielib
import time

url = 'http://www.baidu.com'

print('first one')
response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))
time.sleep(5)

print('second one')
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
response2 = urllib2.urlopen(request)
print(response2.getcode())
print(len(response2.read()))
time.sleep(5)

print('third one')
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print(response3.read())
print(response3.getcode())
print(cj)
