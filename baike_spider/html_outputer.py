#coding=utf-8
class HtmlOutputer():
  def __init__(self):
    self.datas = []

  def collect_data(self, data):
    if data is None:
      return
    self.datas.append(data)

  def output_html(self):
    fout = open('spider_output.html', 'w')
    fout.write("<html>")
    fout.write("<body>")

    fout.write("<table>")
    for data in self.datas:
      fout.write("<tr>")
      # fout.write("<td>%s</td>" % data['url'])
      fout.write("<td><a href='%s'>%s</a></td>" % (data['url'].encode('utf-8'), data['title'].encode('utf-8')))
      fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
      fout.write("</tr>")

    fout.write("</table>")

    fout.write("</body>")
    fout.write("</html>")

  def output_json(self):
    fout = open('spider_out_put.json', 'w')
    fout.write('[')
    count = 1
    for data in self.datas:
      fout.write('{')
      fout.write('"url":"%s",' % data['url'])
      fout.write('"title":"%s",' % data['title'].encode('utf-8'))
      fout.write('"summary":"%s"' % data['summary'].encode('utf-8').replace('\n', '').replace('\r', ''))
      if count == len(self.datas):
        fout.write('}')
      else:
        fout.write('},')
      count = count + 1
    fout.write(']')
