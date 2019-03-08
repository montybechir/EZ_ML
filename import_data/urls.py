from django.conf.urls import url
from import_data import views
from django.urls import path
urlpatterns = [
    url(r'^$', views.ImportHomePage.as_view(), name='ImportHomePage'),
    path('upload/', views.upload, name= 'upload') # references upload function in views
]