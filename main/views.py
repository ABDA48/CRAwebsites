from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import News,Gallerie,ImageGallerie,Video,Book
def dashboard(response):
    return render(response,"main/dashboard.html",{}) 


def myFunc(e):
  return e['created_at']
def FunActualite():
    actualite=list(News.objects.all().values())
    actualite.sort(key=myFunc,reverse=True)
    act=[]
    if len(actualite)>=4:
        act=actualite[:4]   
    else:
        act=actualite
    return act

def FunGallerie():
    gallerie=list(Gallerie.objects.all().values())
    gallerie.sort(key=myFunc,reverse=True)
    gal=[]
    if len(gallerie)>=6:
        gal=gallerie[:6]   
    else:
        gal=gallerie
    return gal
def FunVideo():
    video=list(Video.objects.all().values())
    video.sort(key=myFunc,reverse=True)
    vid=[]
    if len(video)>=6:
        vid=video[:6]   
    else:
        vid=video
    return vid

    
def home(response):
    act=FunActualite()
    gal=FunGallerie()
    vid=FunVideo()
    return render(response,"main/home.html",{"act":act,"gal":gal,"vid":vid}) 


def actualite(response):
    actualite=list(News.objects.all().values())

    return render(response,'main/actualite.html',{'ls':actualite})



def video(response):
    video=list(Video.objects.all().values())
    return render(response,'main/video.html',{'ls':video})

def gallerie(response):
    gallerie=list(Gallerie.objects.all().values())

    galleriePhotos=[]
    for g in gallerie:
        images=[]
        id=g["id"]
        im=list(ImageGallerie.objects.filter(idgallerie=id).values())
        for i in im:
            images.append(i["imageprofile"])
        gl={}
        gl["id"]=g["id"]
        gl["title"]=g["title"]
        gl["subtitle"]=g["subtitle"]
        gl["description"]=g["description"]
        gl["photos"]=images
        galleriePhotos.append(gl)
    
   
        
    
    return render(response,'main/gallerie.html',{'ls':galleriePhotos,})


def livre(response):
    livre=list(Book.objects.all().values())

    return render(response,'main/livre.html',{'ls':livre})

def viewFile(response,id):
    pdf=Book.objects.get(pk=id)
    bkt=pdf.title
    bks=pdf.subtitle
    bkurl=pdf.doc.url
    bk={"url":bkurl,"sub":bks,"title":bkt}
    return render(response,'main/viewFile.html',{'ls':bk})