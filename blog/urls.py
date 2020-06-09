from django.urls import path
from . import views
app_name='blog'
#Here the urls paths of the blog is defined
urlpatterns = [
    path('',views.home,name='home_page'),
]
