from . import views
from django.urls import path
from django.conf import settings
imo

urlpatterns = [
    path('',views.PostList.as_view(), name = 'home'),
    path('<slug:slug>/', views.Postdetail, name = 'post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)