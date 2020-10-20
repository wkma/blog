from django.test import TestCase

# Create your tests here.
# from django.db.models.functions import TruncMonth
#     Sales.objects\
#     .annocate(month=TruncMonth('timetamp'))\  #将日期按照月份截取出来并添加到列表
#     .values('month')  #group by month
#     .annocate(c=Count('id'))  #select the count of the grouping选择分组的计数
#     .values('month','c')   #(might be redundant,haven't tested) select month and count可能是多余的，尚未测试）选择月份和计数