#!/usr/bin/env python
#coding:utf-8

from django.db import models
from django.core.urlresolvers import reverse

class Article(models.Model):
    title = models.CharField(max_length = 100) #博客标题
    category = models.CharField(max_length = 50, blank = True) #博客标签
    date_time = models.DateTimeField(auto_now_add = True) #博客日期
    content = models.TextField(blank = True, null = True) #博客文章正文

    #获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://192.168.4.2%s" % path
    #python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title

    #按时间降序排序
    class Meta:
        ordering = ['-date_time']
