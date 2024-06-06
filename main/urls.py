from django.urls import path
from main import views
urlpatterns = [
    path('',views.home,name='home'),
  
      path('actualite/',views.actualite,name='actualite'),
       path('video/<str:id>',views.videodetail,name='videodetail'),
       path('video/',views.video,name='video'),
       path('gallerie/',views.gallerie,name='gallerie'),
             path('livre/',views.livre,name='livre'),
             path('livre/<str:id>',views.livredetail,name='livredetail'),
             path('viewFile/<int:id>',views.viewFile,name='viewFile'),




              path('news/<str:id>',views.news,name='news'),
              path('newslists/',views.newsView,name='newslists'),

              path("photos/",views.photos,name='photos'),
             path("news_filter/",views.news_filter,name='news_filter'),
 path("books_filter/",views.books_filter,name='books_filter'),
               path("video_filter/",views.video_filter,name='video_filter'),
                path("rvs/",views.rvs,name='rvs'),
                 path("infopro/",views.infopro,name='infopro'),
                        path("iframe/<str:id>",views.iframe,name='iframe'),
                  

]