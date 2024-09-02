from django.contrib import admin
from django.urls import path

from django.urls import include, path

from news import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршруты для панели администратора
    #path('', views.index, name='index'),  # Маршрут для главной страницы приложения news
    path('news/', include('news.urls'))
]





