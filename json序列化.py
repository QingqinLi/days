# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import json

from datetime import datetime, time, date

from django.core import serializers


data = [
    {"pk": 1, "name": "\u83b9\u83b9", "age": 18, 'birth': datetime.now()},
    {"pk": 2, "name": "\u5c0f\u5fae", "age": 16, 'birth': datetime.now()},
    {"pk": 3, "name": "\u5c0f\u9a6c\u54e5", "age": 8, 'birth': datetime.now()},
    {"pk": 4, "name": "qqq", "age": 5, 'birth': datetime.now()},
    {"pk": 5, "name": "www", "age": 5, 'birth': datetime.now()}
]


# data = serializers.serialize("json", data)

# datetime类型不可以json序列化
# print(json.dumps(data))


# 自定义
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)

print(json.dumps(data, cls=JsonCustomEncoder))
