from django.contrib.auth.models import User
from news.models import Author, Category, Post  

with open('results.py', 'w', encoding='utf-8') as f:
    # Запросы и запись результатов в файл
    authors = Author.objects.all()
    f.write("Авторы:\n")
    for author in authors:
        f.write(f"Имя пользователя: {author.user.username}, Рейтинг: {author.rating}\n")

    categories = Category.objects.all()
    f.write("\nКатегории:\n")
    for category in categories:
        f.write(f"Название категории: {category.name}\n")

    posts = Post.objects.all()
    f.write("\nПосты:\n")
    for post in posts:
        f.write(f"Заголовок: {post.title}, Тип: {post.get_type_display()}, Рейтинг: {post.rating}\n")

print("Результаты запросов сохранены в файл results.txt")
