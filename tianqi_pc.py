import requests
from bs4 import BeautifulSoup


def pares_page(url):
    summys=[]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    responses = requests.get(url=url, headers=headers)
    # print(responses.content.decode("utf-8"))
    soup = BeautifulSoup(responses.content.decode("utf-8"), "lxml")
    conMidtab = soup.find('div', attrs={'class': 'conMidtab'})
    tables = conMidtab.find_all("table")
    for table in tables:
        trs = table.find_all("tr")[2:]
        for index,tr in enumerate(trs):
            print(index)
            if index ==0:
                tds = tr.find_all("td")
                city_td = tds[1]
                temp_td = tds[7]
            else:
                tds = tr.find_all("td")
                city_td = tds[0]

                temp_td = tds[6]
            temp = list(temp_td.stripped_strings)[0]
            city = list(city_td.stripped_strings)[0]
            summy ={
                'city':city
                ,'temp':temp
            }
            summys.append(summy)
    print(summys)
    return summys
        # city_td =tr[0].find_all('td')[0]
        # city = list(city_td.stripped_strings)
        # print(city)


def main():
    url = "http://www.weather.com.cn/textFC/hz.shtml"
    pares_page(url)


if __name__ == '__main__':
    print(main())


