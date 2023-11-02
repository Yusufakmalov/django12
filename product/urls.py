from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import index_html, article_page
from product import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_html),
    path('statya', article_page),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)