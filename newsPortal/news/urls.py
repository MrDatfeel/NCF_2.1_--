from django.urls import path, include
from . import views
from .views import subscribe

urlpatterns = [
    # Существующие маршруты
    path('', views.news_list, name='news_list'),
    path('<int:article_id>/', views.news_detail, name='news_detail'),

    # Маршруты для новостей
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),

    # Маршруты для статей
    path('articles/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),

    # Маршруты для профиля
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile'),

    # Маршруты для аутентификации и регистрации
    path('accounts/', include('allauth.urls')),  # Включает все маршруты для django-allauth

    # Дополнительные маршруты для социальных входов и регистрации (если нужны)
    # path('accounts/social/', include('allauth.socialaccount.urls')),  # Включает маршруты для социальных аккаунтов
    path('categories/<int:pk>', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]







