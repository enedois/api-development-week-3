from django.urls import path
from . import views


urlpatterns =[

path('', views.getData),
path('single/<int:pk>',views.item_detail),
path('add/',views.postData),
path('update/<int:pk>',views.updateData),
path('delete/<int:pk>',views.deleteData),


]