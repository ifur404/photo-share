from django.urls import path
from .views import index,addphoto,addcategory,viewphoto,deletephoto

urlpatterns = [
    path('', index, name='index'),
    path('addphoto/', addphoto, name='addphoto'),
    path('addcategory/', addcategory, name='addcategory'),
    path('deletephoto/<str:pk>/', deletephoto, name='deletephoto'),
    path('photo/<str:pk>/', viewphoto, name='viewphoto'),
]
