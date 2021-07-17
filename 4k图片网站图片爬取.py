#-*- codeing=utf-8 -*-
#@time : 2021/7/17 下午3:05
#@Author : zuoyoupeng
#@File: 4k图片网站图片爬取.py
#@Software:PyCharm

#4k图片网站图片爬取

import requests
from lxml import etree
import os

def get_picture():
    try:
        url = "https://pic.netbian.com/4kdongman/index_2.html"
        headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
        html_pic = requests.get(url=url, headers=headers)
        html_pic.encoding = 'gb2312'
        html_text = html_pic.text
        # print(html_text)
        etree_html = etree.HTML(html_text)
        li_list = etree_html.xpath('//div[@class="slist"]/ul/li')
        path = './pictures'
        if not os.path.exists(path):
            os.mkdir(path)
        for li in li_list:
            pic_add = "https://pic.netbian.com/" + li.xpath("./a/img/@src")[0]
            pic_name = li.xpath("./a/img/@alt")[0] + '.jpg'
            img_data = requests.get(url=pic_add, headers=headers).content
            img_path = path + '/'+pic_name
            with open(img_path,'ab') as fp:
                fp.write(img_data)
                print(pic_name, "保存成功！")
    except:
        return "产生异常"


def main():
    get_picture()

if __name__ == '__main__':
    main()


