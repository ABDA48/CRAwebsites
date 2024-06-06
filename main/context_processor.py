from .models import News,Gallerie,ImageGallerie,Video,Book
def default(response):
    news=News.objects.all()
    context={
      "newsUrl":news
    }
    return(context)