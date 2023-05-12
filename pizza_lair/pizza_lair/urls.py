from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('offers/', include('offers.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
