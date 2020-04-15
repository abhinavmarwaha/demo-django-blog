from django.conf.urls import url
from django.contrib import admin
from djangoo.urls


urlpatterns = [
    path(r'^admin/', admin.site.urls),

]
