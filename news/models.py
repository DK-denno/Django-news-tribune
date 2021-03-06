from django.db import models
import datetime as dt

# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering=['-first_name']

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    article_image = models.ImageField(upload_to = 'articles/')
    publishedAt = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_news(cls):
        today = dt.datetime.today()
        article = cls.objects.filter(publishedAt__date=today)
        return article
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(publishedAt__date = date)
        return news
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    def __str__(self):
        return self.title

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.name
        