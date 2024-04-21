from django import forms

from .models import Article, Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'categories_id']
        labels = {'name': 'Название овоща', 'text': 'Описание овоща',
                  'categories_id':'Категория'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'text': forms.Textarea(attrs={'rows': 10, 'cols': 100, 'class': 'form-control'})}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_category']
        labels = {'name_category': 'Название категории'}