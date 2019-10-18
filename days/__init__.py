from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from my_signals import pizza_dome


# def callback(sender, **kwargs):
#     """
#     固定写法
#     :param sender:
#     :param kwargs:
#     :return:
#     """
#     print("xxoo_callback")
#     print(sender, kwargs)
#
#
# post_save.connect(callback)


# 方法二
# @receiver(post_save)
# def my_callback(sender, **kwargs):
#     print("my_callback")
#     print(sender, kwargs)
#

@receiver(pizza_dome)
def my_callback1(sender, **kwargs):
    print("my_callback1")
    print(sender, kwargs)