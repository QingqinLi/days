# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 自定义信号
import django.dispatch
pizza_dome = django.dispatch.Signal(providing_args=["a", "b"])