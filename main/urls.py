from django.urls import path
from main import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('home/',views.home,name='home'),
      path('actualite/',views.actualite,name='actualite'),
       path('video/',views.video,name='video'),
       path('gallerie/',views.gallerie,name='gallerie'),
             path('livre/',views.livre,name='livre'),
             path('viewFile/<int:id>',views.viewFile,name='viewFile'),

]