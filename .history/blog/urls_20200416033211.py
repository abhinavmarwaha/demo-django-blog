from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))

]
