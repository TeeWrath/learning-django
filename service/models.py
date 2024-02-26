from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Service(models.Model) :
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=HTMLField()

# Model for news
class News(models.Model) :
    news_title = models.CharField(max_length=100)
    news_desc = HTMLField()
    news_slug = AutoSlugField(populate_from='news_title', unique=True,null=True,default=None)