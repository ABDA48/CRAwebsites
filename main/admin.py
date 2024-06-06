from django.contrib import admin
from .models import News,Gallerie,ImageGallerie,Video,Book,PlayList
from django.contrib.auth.models import User
from django import forms

"""
news(id,img1,img2,img3,title,subtitle,headline,description)
gallerie(id,img,title,subtitle,description,photos)
video(id,link,title,subtitle)
book(id,pdf,img,title)

"""

class NewsAdmin(admin.ModelAdmin):

    list_display=['id','news_img','title','headline','news_description',"created_at"]
    search_fields=('title','headline','id' )
    list_filter=('id',"created_at",'title')
    
 
class ImageGallerieAdmin(admin.TabularInline):
    model=ImageGallerie


class GallerieAdmin(admin.ModelAdmin):
    inlines=[ImageGallerieAdmin]
    list_display=['id','gal_img','title','subtitle','description']
   

class PlayListAdmin(admin.ModelAdmin):
    list_display=('id','description','title')
    search_fields=('id','description','title')


class VideoAdmin(admin.ModelAdmin):
    list_display=('id','link','title')
    search_fields=('id','title', )

class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','img_bk')
    search_fields=('id','title')

 
admin.site.register(News,NewsAdmin),
admin.site.register(Gallerie,GallerieAdmin),
admin.site.register(Video,VideoAdmin),
admin.site.register(Book,BookAdmin),
admin.site.register(PlayList,PlayListAdmin),

