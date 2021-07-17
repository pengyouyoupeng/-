#-*- codeing=utf-8 -*-
#@time : 2021/7/17 下午3:32
#@Author : zuoyoupeng
#@File: 简历模板爬取.py
#@Software:PyCharm

# 简历模板爬取

import requests
from lxml import etree
import os





def main():
    url = "https://sc.chinaz.com/jianli/free.html"
    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    down_data(url, headers)
    url_set = set()
    # 把每一页的url放到一个容器里(有待完善，不能爬取足够多的网址，比如789页)
    url_set = get_url(url, headers, url_set)
    for urll in url_set:
        down_data(urll, headers)



def down_data(url,headers):
    try:
        html_ = requests.get(url=url, headers=headers)
        html_.encoding = 'utf-8'
        html_text = html_.text
        html_tree = etree.HTML(html_text)
        loadadd_lable_list = html_tree.xpath('//div[@id="container"]/div/a')
        loadadd_list = []
        for lable in loadadd_lable_list:
            loadadd_list.append(lable.xpath('./@href'))
        if not os.path.exists('./jianli'):
            os.mkdir('./jianli')
        for loadadd in loadadd_list:
            url = "https:" + loadadd[0]
            html_2 = requests.get(url=url, headers=headers)
            html_2.encoding = 'utf-8'
            etree_html = etree.HTML(html_2.text)
            loadfilename = etree_html.xpath("//div[@class='ppt_tit clearfix']/h1/text()")
            loadpath = "jianli/" + loadfilename[0] + ".rar"
            data_address = etree_html.xpath('//div[@class="down_wrap"]//li[1]/a/@href')[0]
            print(data_address)
            jianli_data = requests.get(url=data_address, headers=headers).content
            with open(loadpath, "ab") as fp:
                fp.write(jianli_data)
                print(loadfilename[0], "保存成功！")
    except:
        print("产生异常")

def get_url(url,headers,url_set):#此函数有待完善，缺点是只能爬取第一页的几个分页链接
    #其实这个也应该使用try-except
    html_text = requests.get(url = url ,headers = headers ).text
    html_tree = etree.HTML(html_text)
    lable_list = html_tree.xpath('//div[@class="pagination fr clearfix clear"]/a')
    for lable_ in lable_list[2:7]:
        lable_url = "https://sc.chinaz.com/jianli/" + lable_.xpath("./@href")[0]
        url_set.add(lable_url)
    return url_set



if __name__ == '__main__':
    main()

