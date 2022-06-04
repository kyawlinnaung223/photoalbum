
from  django.urls import path
from .import views

urlpatterns=[
          path('',views.gallerypageivew,name="gallery"),
          path('photo/<str:pk>/',views.photopageview,name="photo-page"),
          path('add',views.addpageview,name="add-page"),
]