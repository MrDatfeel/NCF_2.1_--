from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment, Article, News

# Настройка админки для модели Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')  # Поля, которые отображаются в списке
    search_fields = ('user__username',)  # Поля, по которым можно искать

# Настройка админки для модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля, которые отображаются в списке
    search_fields = ('name',)  # Поля, по которым можно искать

# Настройка админки для модели Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'created_at', 'rating')  # Поля, которые отображаются в списке
    list_filter = ('type', 'created_at')  # Фильтры для боковой панели
    search_fields = ('title', 'author__user__username')  # Поля, по которым можно искать
    #filter_horizontal = ('categories',)  # Горизонтальный фильтр для ManyToManyField

# Настройка админки для модели PostCategory
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')  # Поля, которые отображаются в списке
    list_filter = ('category',)  # Фильтры для боковой панели
    search_fields = ('post__title',)  # Поля, по которым можно искать

# Настройка админки для модели Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'rating')  # Поля, которые отображаются в списке
    list_filter = ('created_at',)  # Фильтры для боковой панели
    search_fields = ('user__username', 'post__title')  # Поля, по которым можно искать

# Настройка админки для модели Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  # Поля, которые отображаются в списке
    search_fields = ('title',)  # Поля, по которым можно искать

# Настройка админки для модели News
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # Поля, которые отображаются в списке
    search_fields = ('title', 'author__username')  # Поля, по которым можно искать

# Регистрация моделей с настройками в админке
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
