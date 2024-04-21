from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:categories_id>/', views.category, name='category'),
    # path('articles/', views.articles, name='articles'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('info/', views.info, name='info'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_category/', views.add_category, name='add_category')
]