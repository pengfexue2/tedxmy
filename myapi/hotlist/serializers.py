#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-11-18 16:19

__author__ = 'Ted'


from rest_framework import serializers
from .models import Website, Weibo


class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('CreateTime','Desc','Title','Url','approvalNum','commentNum','hotDesc','idWeb','imgUrl')


class WeiboSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weibo
        fields = ('CreateTime','index','title','mark','level','link')
