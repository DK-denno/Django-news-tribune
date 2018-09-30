from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article,tags,Editor

# Create your views here.
def welcome(response):
    return render(response,'welcome.html')

def convertdates(today):
    '''
    this function get the weekday number for the date
    '''
    daye = dt.date.weekday(today)
    days = ['Monday','Teusday','Wednesday','Thursday','Friday','Saturday','Sunday']
    '''
    function to return the actual day name
    '''
    day = days[daye]
    return day
def archives(request,past_date):

    try:
        date = dt.datetime.strptime(past_date,"%Y-%m-%d").date()
    except ValueError:
        #raise valueError
        raise Http404()

    if date == dt.datetime.today():
        return redirect(news_of_day)

    news = Article.days_news(date)

    return render(request,'all-news/past.html',{"news":news,"dennis":date})


def news_of_day(request):
    date = dt.datetime.today()
    news = Article.todays_news()
    return render(request,'all-news/today.html',{"dennis":date,'news':news})

def search_results(request):
    if 'article' in request.GET or request.GET['article']:
        search_item = request.GET.get('article')
        searched_articles = Article.search_by_title(search_item)
        print(searched_articles)
        message = f"{search_item}"
        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article}) 
