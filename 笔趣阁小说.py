#-*- codeing=utf-8 -*-
#@time : 2021/7/17 下午2:50
#@Author : zuoyoupeng
#@File: 笔趣阁小说.py
#@Software:PyCharm

# 笔趣阁小说及其网址爬取
import requests
from lxml import etree

#

url = "https://www.xbiquge.la/"
headers= {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}


def main():
    html_text = requests.get(url=url, headers=headers).text
    # 先实例化一个etree对象
    html_etree_object = etree.HTML(html_text)
    passage_title_list1 = html_etree_object.xpath("//div/dl/dt/a[@href]")
    passage_addre_list1 = html_etree_object.xpath("//dt/a/@href")

    # print(passage_title_list1)
    # print(passage_addre_list1)
    with open('data.txt','w',encoding='utf-8') as fp:
        for (ti,ad) in zip(passage_title_list1,passage_addre_list1):
            fp.write(ti.xpath("./text()")[0] + ":" + ad+'\n')





if __name__ == '__main__':
    main()