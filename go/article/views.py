from django.shortcuts import render, redirect
from .forms import ArticleForm, CategoryForm
from .models import Article, Category


def home(request):
    return render(request, 'article/home.html')

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article/article.html', context={'article': article})

def articles(request):
    articles = list(Article.objects.order_by('name'))
    return render(request, 'article/articles.html', context={'articles': articles})

def info(request):
    return render(request, 'article/info.html')

def add_article(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:home')
    return render(request, 'article/add_article.html', context={'form': form})

def add_category(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:home')
    return render(request, 'article/add_category.html', context={'form': form})

def categories(request):
    categories = Category.objects.all().order_by('name_category')
    context = {'categories': categories}
    return render(request, 'article/categories.html', context=context)

def category(request, categories_id):
    category = Category.objects.get(id=categories_id)
    articles = category.articles.all().order_by('name')
    context = {'category': category, 'articles': articles}
    return render(request, 'article/category.html', context=context)


