from django.db import models

# Create your models here.
"""
先写普通字段，再写外键字段
"""
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.IntegerField(verbose_name="手机号",null=True,blank=True)
    #null=true表示数据库字段可以为空，blank=True，admin后台字段可以为空
    avatar = models.FileField(upload_to='avatar/',default='avatar/default.png')#头像
    """
    给avatar字段传文件对象，该文件会自动存储到avatar文件下，然后avatar字段只保存文件路径avatar/dafault.png
    """
    create_time = models.DateField(auto_now_add=True)

    blog = models.OneToOneField(to='Blog',null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="用户信息"

    def __str__(self):
        return self.username


class Blog(models.Model):
    site_name = models.CharField(verbose_name="站点名称",max_length=32)
    site_title = models.CharField(verbose_name="站点标题",max_length=32)
    site_theme = models.CharField(verbose_name="站点样式",max_length=64)  #存CSS/JS的文件路径，模拟多背景样式操作

    class Meta:
        verbose_name_plural ="个人站点"

    def __str__(self):
        return self.site_name


class Category(models.Model):
    name = models.CharField(verbose_name="文章分类",max_length=32)
    blog = models.ForeignKey(to='Blog',null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="分类"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name="标签",max_length=32)
    blog = models.ForeignKey(verbose_name="站点名称",to='Blog',null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="标签"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name="文章标题",max_length=255)
    desc = models.CharField(verbose_name="文章简介",max_length=255)
    #文章内容有很多，一般使用TextField
    content = models.TextField(verbose_name="文章内容")
    create_time = models.DateField(auto_now_add=True)
    # 数据库字段设计优化
    up_num = models.IntegerField(verbose_name="点赞数", default=0)
    down_num = models.IntegerField(verbose_name="点踩数", default=0)
    comment_num = models.BigIntegerField(verbose_name="评论数", default=0)
    #外键字段
    blog = models.ForeignKey(to='Blog',null=True,on_delete=models.CASCADE,verbose_name="个人站点")
    category = models.ForeignKey(to='Category',null=True,on_delete=models.CASCADE,verbose_name="分类")
    tags = models.ManyToManyField(to='Tag',
                                  through='Article_Tag',
                                  through_fields=('article','tag')
                                  )

    class Meta:
        verbose_name_plural ="文章"

    def __str__(self):
        return self.title

class Article_Tag(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural ="文章标签"


class UpAndDown(models.Model):
    user = models.ForeignKey(to="UserInfo",on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article",on_delete=models.CASCADE)
    is_up = models.BooleanField()  #传布尔值

    class Meta:
        verbose_name_plural ="调整顺序"


class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo',on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article",on_delete=models.CASCADE)
    content = models.CharField(verbose_name="评论内容",max_length=255)
    comment_time = models.DateTimeField(verbose_name="评论时间",auto_now_add=True)
    #自关联
    parent = models.ForeignKey(to='self',null=True,on_delete=models.CASCADE)  #Null=True，因为有些piglet是根评论

    class Meta:
        verbose_name_plural ="评论"

    def __str__(self):
        return self.user