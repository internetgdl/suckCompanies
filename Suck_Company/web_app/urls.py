from django.conf.urls import include,url
from rest_framework import permissions, routers, serializers, viewsets
from . import views
from . import api
from .apiv2 import CompanyViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('companies',CompanyViewSet)
router.register('categories',CategoryViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company_new$', views.companynew, name='company_new'),
    url(r'^api/company/new$', api.company_new, name='api_company_new'),
    url(r'^api/company/search$', api.company_search, name='api_company_search'),
    url(r'^api/', include(router.urls)),
]
