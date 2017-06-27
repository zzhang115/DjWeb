from django.db import models
from mongoengine import *
from mongoengine import connect
from django.core.paginator import Paginator
connect('djweb', host='127.0.0.1', port=27017)

# Create your models here.

class ArticleInfo(Document):
    des = StringField()
    title = StringField()
    score = StringField()
    tags = ListField(StringField())
    meta = {'collection' : 'djinfo1'}

for i in ArticleInfo.objects[:4]: # equal to limit(1)
    print(i.title, i.des, i.score, i.tags)

iter = 'sdfjowejqwjrkwj;efkjdskjf;sj'
paginator = Paginator(iter, 4) # can only display 4 items per page
print(paginator.page(1))
