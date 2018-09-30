from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#importing the views module from the news app
from . import views


urlpatterns=[
    url(r'^$',views.news_of_day,name='newsToday'),
    url(r'^search',views.search_results,name='search_results'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.archives,name = 'pastNews'),
     url(r'^article/(\d+)',views.article,name ='article')

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
