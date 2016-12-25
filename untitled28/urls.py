from django.conf.urls import url
from django.contrib import admin
from eae.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/all/$', all_books.as_view()),
    url(r'^books/(?P<pk>\d+)/$', get_book.as_view())
]


