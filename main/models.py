from django.db import models
from shortuuid.django_fields import ShortUUIDField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
"""
news(id,img1,img2,img3,title,subtitle,headline,description)
gallerie(id,img,title,subtitle,description,photos)
video(id,link,title,subtitle)
book(id,pdf,img,title)

"""
class News(models.Model):
    id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="news",alphabet="abcdf12345",primary_key=True)
    img1=models.ImageField(blank=True,null=True,upload_to="Images/")
    img2=models.ImageField(blank=True,null=True,upload_to="Images/")
    img3=models.ImageField(blank=True,null=True,upload_to="Images/")
     
    title=models.CharField(max_length=100)
    
    headline=models.CharField(max_length=100,null=True,blank=True)
    description=RichTextUploadingField(null=True,blank=True,default='description')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="News"
    
    def news_img(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'% (self.img1.url))
    def news_description(self):
        return mark_safe(self.description)
    
    
    
    def __str__(self):
        return self.title
    

class Gallerie(models.Model):
    id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="gal",alphabet="abcdf12345",primary_key=True)
    img=models.ImageField(blank=True,null=True,upload_to="Gallery/")
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="Galleries"
    
    def gal_img(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'% (self.img.url))
    
    def __str__(self):
        return self.title

class ImageGallerie(models.Model):
    idgallerie=models.ForeignKey(Gallerie,on_delete=models.SET_NULL,null=True)
    imageprofile=models.ImageField(null=True,blank=True,upload_to='Gallery/')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="ImageGallerie"
    
    def img_gl(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'% (self.imageprofile.url))

class PlayList(models.Model):
    id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="play",alphabet="abcdf12345",primary_key=True)
    description=RichTextUploadingField(null=True,blank=True,default='description')
    title=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title   

class Video(models.Model):
    id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="vid",alphabet="abcdf12345",primary_key=True)
    link=models.CharField(max_length=100)
    img=models.ImageField(blank=True,null=True,upload_to="Gallery/")
    playlist=models.ForeignKey(PlayList,on_delete=models.SET_NULL,null=True,blank=True,related_name='video')

    title=models.CharField(max_length=100)
    categoriechoice=(('dine','Dine'),(('generale','Generale')))
    categorie=models.CharField(choices=categoriechoice,max_length=50,blank=True,default='Generale')
    description=RichTextUploadingField(null=True,blank=True,default='description')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.title








class Book(models.Model):
    id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="book",alphabet="abcdf12345",primary_key=True)
    doc=models.FileField(upload_to='Book/')
    title=models.CharField(max_length=100)
    description=RichTextUploadingField(null=True,blank=True,default='description')
    img=models.ImageField(null=True,blank=True,upload_to='Book/')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def img_bk(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'% (self.img.url))

  
    def __str__(self):
        return self.title



class Infoprof(models.Model):
        id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="prof",alphabet="abcdf12345",primary_key=True)
        nom=models.CharField(max_length=100)
        tel=models.CharField(max_length=50)
        description=RichTextUploadingField(null=True,blank=True,default='description')
        def __str__(self):
            return self.nom

class Infocourse(models.Model):
      
      id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="cou",alphabet="abcdf12345",primary_key=True)
      professeur=models.ForeignKey(Infoprof,on_delete=models.SET_NULL,null=True)
      title=models.CharField(max_length=100)
      description=RichTextUploadingField(null=True,blank=True,default='description')
      def __str__(self):
            return self.title



class InfoGal(models.Model):
    id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="info",alphabet="abcdf12345",primary_key=True)
    img=models.ImageField(blank=True,null=True,upload_to="Infopro/")
    title=models.CharField(max_length=100)
    description=RichTextUploadingField(null=True,blank=True,default='description')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="InfoGalleries"
    
    def gal_img(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'% (self.img.url))
    
    def __str__(self):
        return self.title
   


