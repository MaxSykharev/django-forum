import datetime
from tabnanny import verbose
from django.utils import timezone

from statistics import mode
from django.db import models


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('дата')

    def __str__(self):
        return self.article_title

    def was_publish_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta():
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField('name autor', max_length=50)
    comment_text = models.CharField('text comment', max_length=200)

    def __str__(self):
        return self.autor_name

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
