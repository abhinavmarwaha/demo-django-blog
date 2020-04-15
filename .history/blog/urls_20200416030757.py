from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.PostList.as_view())
]
