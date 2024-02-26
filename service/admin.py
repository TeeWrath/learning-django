from django.contrib import admin
from service.models import Service, News

class ServiceAdmin(admin.ModelAdmin) :
    list_display=('service_icon','service_title','service_des')

class NewsAdmin(admin.ModelAdmin) :
    list_display=('news_title','news_desc')

admin.site.register(Service,ServiceAdmin)
admin.site.register(News,NewsAdmin)