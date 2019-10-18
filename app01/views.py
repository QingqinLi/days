from django.shortcuts import render, HttpResponse
from django.views.decorators.cache import cache_page
from app01.models import *
import datetime, time
from my_signals import pizza_dome
# Create your views here.


# 缓存超期时间
@cache_page(3)
def user_list(request):
    now = time.time()
    user = User.objects.all()
    return render(request, 'user_list.html', {'user': user, 'time': now})


def timer(request):
    now = datetime.datetime.now()
    return HttpResponse(now)


def save_data(request):
    # User.objects.create(name='alex', age=43, role_id=1)

    obj = User.objects.filter(id=1).first()
    obj.name = '测试'
    obj.save()
    pizza_dome.send(sender='my_post', a=123, b=112)
    return HttpResponse("保存成功")

from PIL import Image, ImageFont, ImageDraw
import random


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def v_code(request):

    img_obj = Image.new('RGB', (250, 35), random_color())

    # 在该图片对象上生成一个画笔对象
    draw_obj = ImageDraw.Draw(img_obj)

    font_obj = ImageFont.truetype('static/font/kumo.ttf', 28)

    temp = []
    for i in range(5):
        l = chr(random.randint(97, 122))  # 小写字母
        b = chr(random.randint(65, 90))  # 大写字母
        n = str(random.randint(0, 9))

        t = random.choice([l, b, n])
        temp.append(t)

        draw_obj.text((i * 40 + 35, 0), t, fill=random_color(), font=font_obj)

    # 存在内存中， 不是存在硬盘中
    from io import BytesIO
    f1 = BytesIO()
    img_obj.save(f1, format="PNG")
    img_data = f1.getvalue()

    return HttpResponse(img_data, content_type="image/png")