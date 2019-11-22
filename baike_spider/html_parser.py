#coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse
import lxml

class HtmlParser():
  def _get_new_urls(self, url, soup):
    new_urls = set()
    # <a target="_blank" href="/item/%E6%8E%92%E8%A1%8C%E6%A6%9C/4895" data-lemmaid="4895">排行榜</a>
    links = soup.find_all('a', href=re.compile(r'/item/.*'.replace(r'#.*', '').replace(r'?.*', '')))
    for link in links:
      new_url = link['href']
      new_url_full = urlparse.urljoin(url, new_url)
      new_urls.add(new_url_full)
    return new_urls

  def _get_new_data(self, url, soup):
    res_data = {}
    # url
    res_data['url'] = url

    # title <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
    title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
    res_data['title'] = title_node.get_text()

    # summary <div class="lemma-summary" label-module="lemmaSummary">
    summary_node = soup.find('div', class_='lemma-summary')
    res_data['summary'] = summary_node.get_text()

    return res_data


  def parse(self, url, cont):
    if url is None or cont is None:
      return

    soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
    new_urls = self._get_new_urls(url, soup)
    new_data = self._get_new_data(url, soup)
    return new_urls, new_data
    