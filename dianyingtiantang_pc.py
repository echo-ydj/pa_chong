# encoding : utf-8

from lxml import etree
import requests
url = "https://ygdy8.com/html/gndy/dyzz/20190425/58514.html"
responses = requests.get(url)
# print(responses.content.decode("gbk"))
HTML = etree.HTML(responses.content.decode("gbk"))
li = HTML.xpath("//div[@id='Zoom']//p/text()")
print(li)
for i in  li:
    if i!= "":
        if i.startswith("◎年　　代"):  #Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
            print(i.replace("◎年　　代","").strip())  #strip()去除前后空格


from lxml import etree
import requests
#  忽视编码报错 decode("gbk","ignore")
# url = "https://ygdy8.com/html/gndy/dyzz/list_23_3.html"
# resp = requests.get(url)
# print(resp.status_code)
# print(resp.content.decode("gbk","ignore"))

def get_url():
    urls_list=[]
    url = "https://ygdy8.com/html/gndy/dyzz/list_23_"  # 1.html
    for i in range(1,6):
        urls = url+str(i)+".html"

        urls_list.append(urls)
    print(urls_list)
    return urls_list

def get_html(urls):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    response_list=[]
    for url in urls:
        response = requests.get(url=url,headers=headers)
        response_list.append(response)
    print(len(response_list))
    return response_list

def get_xpath():
    move_urls=[]
    for responses in get_html(get_url()):
        print(responses)
        html = etree.HTML(responses.content.decode("gbk","ignore"))
        hrefs = html.xpath("//table[@class='tbspan']//a")
        for i in hrefs:
            lj = i.xpath("@href")[0]
            name = i.xpath("text()")[0]
            url = "https://ygdy8.com"+lj
            move_url={
                "name":name
                ,"url":url}
            move_urls.append(move_url)
    return move_urls



if __name__ == '__main__':
    pass
    # print(get_xpath())
    # print(len(get_xpath()))
