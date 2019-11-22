# coding=utf-8
from bs4 import BeautifulSoup
import json
import requests

class HotPointMain(object):
  def __init__(self):
    self.url = 'http://top.baidu.com/buzz?b=1&fr=20811'
    self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    self.cont = None
    self.datas = []
    self.len = 0

  # 下载网页
  def download(self):
    response = requests.get(self.url, headers=self.headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
      self.cont = response.text
    else:
      print('download failed')
  
  # 解析网页
  def html_parse(self):
    soup = BeautifulSoup(self.cont, 'html.parser')
    list_num_nodes = soup.find_all('td', class_='first')
    list_keyword_nodes = soup.find_all('a', class_='list-title')
    list_hit_nodes = soup.find_all('td', class_='last')
    while len(list_num_nodes) != 0:
      data = {}
      data['num'] = list_num_nodes.pop().get_text().replace('\n', '').replace('\r', '')
      data['hits'] = list_hit_nodes.pop().get_text().replace('\n', '').replace('\r', '')
      key_node = list_keyword_nodes.pop()
      data['keyword'] = key_node.get_text()
      print(data['keyword'])
      data['url'] = key_node['href']
      self.datas.append(data)
      self.len = self.len + 1

  # 输出json
  def output_json(self):
    fout = open('hot_points.json', 'w')
    fout.write('[')
    while len(self.datas) != 0:
      data = self.datas.pop()
      fout.write('{')
      fout.write('"num":"%s",' % data['num'])
      fout.write('"url":"%s",' % data['url'])
      fout.write('"keyword":"%s",' % data['keyword'].encode('utf-8'))
      fout.write('"hits":"%s"' % data['hits'])
      fout.write('}')
      if len(self.datas) != 0:
        fout.write(',')
    fout.write(']')

# main函数
if __name__ == '__main__':
  hot_points = HotPointMain()
  hot_points.download()
  hot_points.html_parse()
  hot_points.output_json()