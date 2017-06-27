from django.db import models
from mongoengine import *
# Create your models here.

class ArticleInfo(Document):
    des = StringField() # des its name must be same with it in html
