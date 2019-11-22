#coding=utf-8
import urllib2

class HtmlDownloader():
  def download(self, url):
    if url is None:
      return None

    # request = urllib2.Request(url)
    # request.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    # response = urllib2.urlopen(request)

    response = urllib2.urlopen(url)

    if response.getcode() != 200:
      return None

    return response.read()