from django.test import TestCase

# Create your tests here.
# from django.db.models.functions import TruncMonth
#     Sales.objects\
#     .annocate(month=TruncMonth('timetamp'))\  #将日期按照月份截取出来并添加到列表
#     .values('month')  #group by month
#     .annocate(c=Count('id'))  #select the count of the grouping选择分组的计数
#     .values('month','c')   #(might be redundant,haven't tested) select month and count可能是多余的，尚未测试）选择月份和计数

import os
import sys

if __name__ == "__main__":
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test12_bbs.settings')
    import django

    django.setup()  # 前几行测试时需引用
    from app01 import models

    first = models.UserInfo.objects.filter(pk=1).first()  #查询用户表中主键为1的用户
    print(first)
    #删除对应的文章
    # second_obj = models.Article.objects.filter(title="删除练习").first().delete()
    # print(second_obj)




