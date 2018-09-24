from django.conf.urls import url

#importing the views module from the news app
from . import views

urlpatterns=[
    url('^$',views.welcome, name = 'welcome'),
    url('^today/$',views.news_of_day,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.archives,name = 'pastNews'),
    url('^x/$',views.news_of_day, name='w'),

    
]
