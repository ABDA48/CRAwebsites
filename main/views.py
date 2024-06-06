from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import News,Gallerie,ImageGallerie,Video,Book,PlayList
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Count,Avg,Q
from collections import defaultdict
from django.core.paginator import Paginator

from django.http import FileResponse


def myFunc(e):
  return e['created_at']
def FunActualite(nb):
    actualite=list(News.objects.all().values())
    actualite.sort(key=myFunc,reverse=True)
    act=[]
    if len(actualite)>=nb:
        act=actualite[:nb]   
    else:
        act=actualite
    return act

def news(response,id):
    act=FunActualite(10)
    actual=News.objects.get(id=id)
    return render(response,"main/news_detail.html",{"act":act,"actual":actual})

def FunGallerie(nb):
    gallerie=list(Gallerie.objects.all().values())
    gallerie.sort(key=myFunc,reverse=True)
    gal=[]
    if len(gallerie)>=nb:
        gal=gallerie[:nb]   
    else:
        gal=gallerie
    return gal
def FunVideo(nb):
    video=list(Video.objects.all().values())
    video.sort(key=myFunc,reverse=True)
    vid=[]
    if len(video)>=nb:
        vid=video[:nb]   
    else:
        vid=video
    return vid
def home(response):
    act=FunActualite(5)
    gal=FunGallerie(10)
    videogenerale=Video.objects.filter(categorie='generale').order_by('-created_at')[:6]
    videodine=Video.objects.filter(categorie='dine').order_by('-created_at')[:6]
    book=Book.objects.all().order_by('-created_at')[:6]
    context={
       "act":act,"gal":gal,"videogenerale":videogenerale,"videodine":videodine,'books':book
    }
   
    return render(response,"main/index.html",context) 
    



def actualite(response):
    actualite=News.objects.all()
   
    return render(response,'main/actualite.html',{'ls':actualite})

def photos(response):
    act=FunActualite(5)
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
    
    page=Paginator(galleriePhotos,4)
    pnum=response.GET.get("page")
    page_obj=page.get_page(pnum)

    
    return render(response,'main/photos.html',{"act":act,'ls':page_obj,})

def video(response):
    video=[]
    vid=FunVideo(10)
    videoPlaylist = defaultdict(list)
    for result in Video.objects.order_by('playlist'):
        if result.playlist is not None:
            videoPlaylist[result.playlist].append(result)
        else:
            video.append(result)

    
    print(dict(videoPlaylist))
    
     

    
    return render(response,"main/video.html",{"video":video,"vid":vid,"videoPlaylist":dict(videoPlaylist)})

def videodetail(response,id):
    video=Video.objects.get(id=id)
    vid=FunVideo(10)
    return render(response,'main/video_detail.html',{'video':video,"vid":vid})

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


def viewFile(response,id):
    pdf=Book.objects.get(pk=id)
    bkt=pdf.title
    bks=pdf.subtitle
    bkurl=pdf.doc.url
    bk={"url":bkurl,"sub":bks,"title":bkt}
    return render(response,'main/viewFile.html',{'ls':bk})

def newsView(response):
    news=News.objects.all().order_by("-created_at")
    paginator=Paginator(news,9)

    page_number = response.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(response,"main/news.html",{"news":page_obj})

def news_filter(response):
    n=response.GET['news']
    c1=Q(headline__contains=n)
    c2=Q(title__contains=n)
    newsV=News.objects.filter(c1 or c2).order_by("-created_at")

    data=render_to_string("main/singleNews.html",{"news":newsV})
    print(newsV)

    return JsonResponse({"data":data})


def video_filter(response):
    n=response.GET['video']
    c1=Q(title__contains=n)
    videoV=Video.objects.filter(c1).order_by("-created_at")

    data=render_to_string("main/singleVideo.html",{"video":videoV})
    print(videoV)

    return JsonResponse({"data":data})

def books_filter(response):
    n=response.GET['books']
    c1=Q(title__contains=n)
    book=Book.objects.filter(c1).order_by("-created_at")

    data=render_to_string("main/singleBook.html",{"books":book})
    print(book)

    return JsonResponse({"data":data})



def rvs(response):
    return render(response,"main/rvs.html",{})


def infopro(response):
    return render(response,"main/infopro.html",{})

def livredetail(response,id):
    books=Book.objects.all().order_by('-created_at')
    book=Book.objects.get(id=id)
    

    return render(response,"main/livredetail.html",{"books":books,"book":book})

def livre(response):
    books=Book.objects.all().order_by('-created_at')
    return render(response,'main/livredetail.html',{"books":books})

    
def iframe(response,id):
    book=Book.objects.get(id=id)
    with open(book.doc.path, 'rb') as pdf:
        response = FileResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=livreIslamic.pdf'
        return response
   
    
       
         
    




