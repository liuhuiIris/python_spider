#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import time

class BeautifulPictures():
  def __init__(self):
    self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    self.web_url = 'https://www.darryring.com/darry_ring/'
    self.folder_path = '/Users/cloudwiz/Desktop/python_project/DR_Pictures'
    self.class_name = 'img_main'
    self.tag = 'src'
  
  def request(self):
    r = requests.get(self.web_url, headers=self.headers)
    return r
  
  def mkdir(self, path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
      print('创建名字为', path, '的文件夹')
      os.makedirs(path)
      print('创建成功!')
    else:
      print(path, '文件夹已经存在,不可创建')

  def save_img(self, name): ##保存图片
    print('开始保存图片...')
    img = self.request()
    time.sleep(5)
    file_name = name + '.jpg'
    print('开始保存文件')
    f = open(file_name, 'ab')
    f.write(img.content)
    print(file_name,'文件保存成功！')
    f.close()

  def get_pic(self):
    print('开始网页get请求')
    r = self.request()
    print('开始获取所有img_main标签')
    all_imgs = BeautifulSoup(r.text, 'lxml').find_all('img', class_=self.class_name)
    print('开始创建文件夹')
    self.mkdir(self.folder_path)  #创建文件夹
    print('开始切换文件夹')
    os.chdir(self.folder_path)   #切换路径至上面创建的文件夹
    i = 1 #后面用来给图片命名
    for img in all_imgs:
      print(img)
      img_url = img[self.tag] #img标签中完整的src字符串
      print(img_url, str(i))
      self.save_img(str(i))
      i += 1

imgs = BeautifulPictures()
imgs.get_pic()