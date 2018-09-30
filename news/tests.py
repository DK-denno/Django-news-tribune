from django.test import TestCase
from .models import Article,tags,Editor
import datetime as dt

# Create your tests here.
class EditorTest(TestCase):
    def setUp(self):
        self.new_editor = Editor(first_name='dennis',last_name='kamau',email='dennisveer27@gmail.com')
        self.new_editors = Editor(first_name='paul',last_name='kamau',email='dennisveer27@gmail.com')
       
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_editor,Editor))
    
    def test_save_editor(self):
        self.new_editor.save()
        length = Editor.objects.all()
        self.assertTrue(len(length) > 0)   

    def test_delete(self):
        delete_editor = Editor.objects.filter(id=1)
        delete_editor.delete()
        new_editors = Editor.objects.all()
        self.assertTrue(len(new_editors) == 0)   

    def test_update(self):
        self.new_editors.save()
        self.update_editor = Editor.objects.filter(first_name='paul').update(first_name = 'dk')
        self.updated_editor = Editor.objects.get(first_name='dk')
        self.assertTrue(self.updated_editor.first_name,'dk')
    
class Articletest(TestCase):
    def setUp(self):
        self.editor1 =  Editor(first_name='dennis',last_name='kamau',email='dennisveer27@gmail.com')
        self.editor1.save()
        # time = datetime.datetime.now()
        self.new_article = Article(title='123',post='abcd',editor=self.editor1)
        self.new_article.save()

        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
    
    def test_save_article(self):
        self.editor1.save()
        self.new_article.save()
        length = Editor.objects.all()
        self.assertTrue(len(length) > 0)   

    def test_delete_article(self):
        delete_article = Article.objects.filter(id=1)
        delete_article.delete()
        new_articles = Article.objects.all()
        self.assertTrue(len(new_articles) == 0)   

    def test_update_article(self):
        self.new_article.save()
        self.update_article = Article.objects.filter(title='123').update(title = 'aaabbbcccddd')
        self.updated_article = Article.objects.get(title='aaabbbcccddd')
        self.assertTrue(self.updated_article.title,'aaabbbcccddd')

    def test_get_news(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        dates = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(dates)
        self.assertTrue(len(news_by_date) == 0)



