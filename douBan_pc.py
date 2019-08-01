# encoding : utf-8
import requests
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    # , "Referer": " https://www2.bing.com/"
}
url = "https://movie.douban.com/cinema/nowplaying/beijing/"
responses = requests.get(url=url,headers=headers).text


# parser = etree.HTMLParser(encoding="utf-8")
# html = etree.parse(responses,parser=parser)
# print
html = etree.HTML(responses)
res = html.xpath("//ul[@class='lists']")[0]
# print(res)

lis = res.xpath("./li")
moves = []
for i  in  lis:
    # print(etree.tostring(i,encoding="utf-8").decode("utf-8"))
    title = i.xpath("@data-title")[0]
    data_release = i.xpath("@data-release")[0]
    move = {"title":title,
            "socure":data_release
            }
    moves.append(move)
print(moves)
# for i in moves:
#     print(i["title"])
