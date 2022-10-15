
import requests
from lxml import etree

path='E://python学习/爬虫/05-爬取的图片/'

urls='http://jandan.net/ooxx/MjAyMDA2MjYtMTE1#comments'
          #.format(str(i)) for i in range(1,10)]
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

def get_photo(url):
    html=requests.get(url)
    selector=etree.HTML(html.text)
    photo_urls=selector.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/ol/li[1]/div/div/div[2]/p/img')
    print(photo_urls)
    # for photo_url in photo_urls:
    #     print(photo_urls)


get_photo(urls)