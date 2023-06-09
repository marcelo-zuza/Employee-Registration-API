
from django.contrib import admin
from django.urls import path, include
from api1 import urls
from api1.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include(urls)),
    path('api/', include(router.urls))
]
