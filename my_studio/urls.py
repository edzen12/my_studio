from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.home.urls')),

    path('aboutus/', views.aboutus, name="aboutus"),
    path('teams/', views.team, name="teams"),
    path('portfolio/', views.portfolio, name="portfolios"),
    path('services/', views.service, name="services"),
    path('prices/', views.price, name="prices"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)