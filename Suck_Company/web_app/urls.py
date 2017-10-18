from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company_new$', views.companynew, name='company_new'),
    url(r'^api/company/new$', api.company_new, name='api_company_new'),
    url(r'^api/company/search$', api.company_search, name='api_company_search'),
]