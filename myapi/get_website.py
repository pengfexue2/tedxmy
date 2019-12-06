#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-11-18 17:07

__author__ = 'Ted'


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")


import django
if django.VERSION >= (1,7):
    django.setup()


import requests
import re
from bs4 import BeautifulSoup


def get_zhihu():
    headers={"User-Agent":"","Cookie":""}
    zh_url = "https://www.zhihu.com/billboard"
    zh_response = requests.get(zh_url,headers=headers)

    webcontent = zh_response.text
    soup = BeautifulSoup(webcontent,"html.parser")
    script_text = soup.find("script",id="js-initialData").get_text()
    rule = r'"hotList":(.*?),"guestFeeds"'
    result = re.findall(rule,script_text)

    temp = result[0].replace("false","False").replace("true","True")
    hot_list = eval(temp)
    return hot_list


def get_weibo():
    wb_url = "https://s.weibo.com/top/summary"
    headers = {"User-Agent": "", "Cookie": ""}
    wb_response = requests.get(wb_url, headers=headers)
    webcontent = wb_response.text
    soup = BeautifulSoup(webcontent, "html.parser")
    index_list = soup.find_all("td", class_="td-01")
    title_list = soup.find_all("td", class_="td-02")
    level_list = soup.find_all("td", class_="td-03")

    topic_list = []
    for i in range(len(index_list)):
        item_index = index_list[i].get_text(strip=True)
        if item_index == "":
            item_index = "0"
        item_title = title_list[i].a.get_text(strip=True)
        if title_list[i].span:
            item_mark = title_list[i].span.get_text(strip=True)

        else:
            item_mark = "置顶"
        item_level = level_list[i].get_text(strip=True)
        topic_list.append({"index": item_index, "title": item_title, "mark": item_mark, "level": item_level,
                           "link": f"https://s.weibo.com/weibo?q=%23{item_title}%23&Refer=top"})
    return topic_list


if __name__ == '__main__':
    from hotlist.models import Website, Weibo
    import time
    ted = get_zhihu()
    Website.objects.all().delete()
    count = 0
    for item in ted:
        count+=1
        Website.objects.get_or_create(CreateTime=int(time.time()), Desc=item['target']['excerptArea']['text'], Title=item['target']['titleArea']['text'],Url=item['target']['link']['url'], approvalNum="0", commentNum=str(item['feedSpecific']['answerCount']),hotDesc=item['target']['metricsArea']['text'], idWeb=str(count), imgUrl=item['target']['imageArea']['url'])
    print("zhihu done")

    mia = get_weibo()
    Weibo.objects.all().delete()
    wb_count = 0
    for topic in mia:
        wb_count+=1
        Weibo.objects.get_or_create(CreateTime=int(time.time()), index=topic['index'], title=topic['title'],mark=topic['mark'],level=topic['level'],link=topic['link'])
    print("weibo done")