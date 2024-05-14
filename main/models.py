from django.db import models

"""
news(id,img1,img2,img3,title,subtitle,headline,description)
gallerie(id,img,title,subtitle,description,photos)
video(id,link,title,subtitle)
book(id,pdf,img,title)

"""
class News(models.Model):
    id=models.AutoField(primary_key=True)
    img1=models.ImageField(blank=True,null=True,upload_to="Images/")
    img2=models.ImageField(blank=True,null=True,upload_to="Images/")
    img3=models.ImageField(blank=True,null=True,upload_to="Images/")
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    headline=models.CharField(max_length=100)
    description=models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Gallerie(models.Model):
    id=models.AutoField(primary_key=True)
    img=models.ImageField(blank=True,null=True,upload_to="Gallery/")
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ImageGallerie(models.Model):
    idgallerie=models.ForeignKey(Gallerie,on_delete=models.CASCADE)
    imageprofile=models.ImageField(null=True,blank=True,upload_to='Gallery/')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __int__(self):
        return self.idgallerie

class Video(models.Model):
    id=models.AutoField(primary_key=True)
    link=models.CharField(max_length=100)
    
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.title

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    doc=models.FileField(upload_to='Book/')
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    img=models.ImageField(null=True,blank=True,upload_to='Book/')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.title