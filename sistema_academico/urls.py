from django.contrib import admin
from django.urls import path
from core.views import index

urlpatterns = [
    path('admin/', admin.site.center_admin_site if hasattr(admin.site, 'center_admin_site') else admin.site.urls),
    path('', index, name='index'),
]
