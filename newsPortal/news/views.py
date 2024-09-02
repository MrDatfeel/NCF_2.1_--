from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Article, Profile, Category, Post
from .forms import ArticleForm, ProfileForm



# Существующие представления

def news_list(request):
    """Представление для отображения списка новостей и статей."""
    articles = Article.objects.all()
    return render(request, 'news_list1.html', {'articles': articles})

def news_detail(request, article_id):
    """Представление для отображения деталей конкретной статьи или новости."""
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news_detail.html', {'article': article})

# Новые представления для создания, редактирования и удаления новостей и статей

class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'myapp.add_article'  # Разрешение на создание статьи

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'news'  # Устанавливаем тип "новость"
        return super().form_valid(form)

class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'myapp.add_article'  # Разрешение на создание статьи

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'article'  # Устанавливаем тип "статья"
        return super().form_valid(form)

class NewsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'myapp.change_article'  # Разрешение на изменение статьи

class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'myapp.change_article'  # Разрешение на изменение статьи

class NewsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'myapp.delete_article'  # Разрешение на удаление статьи

class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'myapp.delete_article'  # Разрешение на удаление статьи

# Новые представления для редактирования профиля

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')


class CategoryListView(ListView):
    model = Article
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] =  self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'news/subscribe.html',{'category': category, 'message': message})
