from django.contrib import admin
from .models import News,Gallerie,ImageGallerie,Video,Book
from django.contrib.auth.models import User
from django import forms

"""
news(id,img1,img2,img3,title,subtitle,headline,description)
gallerie(id,img,title,subtitle,description,photos)
video(id,link,title,subtitle)
book(id,pdf,img,title)

"""
class NewsModelForm( forms.ModelForm ):
    class Meta:
        model = News
        fields=['id','img1','img2','img3','title','subtitle','headline','description']
        widgets={
              'description':forms.Textarea(attrs={'cols':100,'rows':100})
          }
class NewsAdmin(admin.ModelAdmin):
    form=NewsModelForm
    list_display=('id','img1','img2','img3','title','subtitle','headline','description')
    search_fields=('title','subtitle','headline','id' )
 
class GallerieModelForm( forms.ModelForm ):
    class Meta:
        model = Gallerie
        fields=['id','img','title','subtitle','description']
        widgets={
              'description':forms.Textarea(attrs={'cols':100,'rows':100})
          }
class GallerieAdmin(admin.ModelAdmin):
    form=GallerieModelForm
    list_display=('id','img','title','subtitle','description')
    search_fields=('title','subtitle','id' )



class VideoAdmin(admin.ModelAdmin):
    list_display=('id','link','title','subtitle')
    search_fields=('id','title','subtitle' )

class BookAdmin(admin.ModelAdmin):
    list_display=('id','title')
    search_fields=('id','title')

admin.site.register(ImageGallerie),
admin.site.register(News,NewsAdmin),
admin.site.register(Gallerie,GallerieAdmin),
admin.site.register(Video,VideoAdmin),
admin.site.register(Book,BookAdmin),