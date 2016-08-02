"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from examples.views import examples_index
from trips.views import trips_home, trips_post_detail
from forms.views import forms_home, forms_thanks
from Simple_CMS.views import CMS_home, CMS_add, CMS_edit, CMS_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', examples_index),

    url(r'^trips/$', trips_home),
    url(r'^trips/post/(?P<pk>\d+)/$', trips_post_detail, name='post_detail'),

    url(r'^forms/$', forms_home),
    url(r'^forms/thanks/$', forms_thanks),

    url(r'^Simple_CMS/$', CMS_home),
    url(r'^Simple_CMS/add$', CMS_add),
    url(r'^Simple_CMS/article/(?P<id>\d+)/edit$', CMS_edit, name = 'CMS_edit'),
    url(r'^Simple_CMS/article/(?P<id>\d+)/$', CMS_detail, name = 'CMS_detail'),

]
