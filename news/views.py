from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(response):
    return render(response,'welcome.html')
def news_of_day(request):
    today = dt.date.today()
    day = convertdates(today)
    html = f'''     
    <html>
            <body>
           <h1>   <b> this is news for  {day} the <b>
               {today.day}th of {today.month} year {today.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

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
    '''
    converting data from the string url
    '''
    today = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convertdates(today)
    html = f'''
        <html>
            <body>
           <h1>   <b> this is news for  {day} the <b>
               {today.day}th of {today.month} year {today.year}</h1>
            </body>
        </html>
        '''
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    if today == dt.date.today():
        return redirect(news_of_day)
    return render(request,'all-news/past.html' ,{"dennis":today},)

def news_of_day(request):
    balling = dt.date.today()
    return render(request,'all-news/today.html',{"dennis":balling,})
