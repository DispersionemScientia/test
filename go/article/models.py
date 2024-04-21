from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=150,  # максимальный размер строки
                            null=False,  # пустые значения хранятся как NULL
                            blank=False, # делает поле не обязательным для заполнения
                            unique=True) # только уникальные значения
    text = models.TextField()
    categories_id = models.ForeignKey('Category', on_delete=models.CASCADE,
                                      related_name='articles')

    def __str__(self):
        return self.name

class Category(models.Model):
    name_category = models.CharField(max_length=40)

    def __str__(self):
        return self.name_category



