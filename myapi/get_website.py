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


if __name__ == '__main__':
    from hotlist.models import Website
    import time
    ted = get_zhihu()
    Website.objects.all().delete()
    count = 0
    for item in ted:
        count+=1
        Website.objects.get_or_create(CreateTime=int(time.time()), Desc=item['target']['excerptArea']['text'], Title=item['target']['titleArea']['text'],Url=item['target']['link']['url'], approvalNum="0", commentNum=str(item['feedSpecific']['answerCount']),hotDesc=item['target']['metricsArea']['text'], idWeb=str(count), imgUrl=item['target']['imageArea']['url'])
    print("done")