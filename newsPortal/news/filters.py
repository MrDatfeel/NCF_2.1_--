import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр по заголовку
    pub_date = django_filters.DateFilter(lookup_expr='gte')  # Фильтр по дате (позже указанной)

    class Meta:
        model = Article
        fields = ['title', 'pub_date']  # Поля, которые будут использоваться для фильтрации
