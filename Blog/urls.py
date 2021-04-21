from django.contrib import admin
from django.urls import path
from blog_one import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('<id>/', views.detail, name = 'detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
