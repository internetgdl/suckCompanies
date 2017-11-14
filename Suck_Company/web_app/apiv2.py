from django.http import HttpResponse
from django.core import serializers
import json
from .models import Company,Category
from .modelsserializers import CompanySerializer, CategorySerializer
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication

class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
