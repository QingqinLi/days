# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import random
from PIL import Image, ImageDraw, ImageFont


def code():
    temp = []
    for i in range(5):
        i = chr(random.randint(97, 122))
        b = chr(random.randint(65, 90))
        n = str(random.randint(0, 9))

        t = random.choice([i, b, n])
        temp.append(t)

    return ''.join(temp)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def code2():
    with open('static/1.png', 'wb') as f:
        img_obj = Image.new('RGB', (250, 35), random_color())
        draw_obj = ImageDraw.Draw(img_obj)

        font_obj = ImageFont.truetype('static/font/kumo.ttf', 29)
        temp = []
        for i in range(5):
            l = chr(random.randint(97, 122))
            b = chr(random.randint(65, 90))
            n = str(random.randint(0, 9))

            t = random.choice([l, b, n])
            temp.append(t)

            draw_obj.text((i*40+35, 0), t, fill=random_color(), font=font_obj)
        img_obj.save(f)

code2()

