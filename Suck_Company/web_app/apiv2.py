from django.http import HttpResponse
from django.core import serializers
import json
from .models import Company,Category
from .modelsserializers import CompanySerializer, CategorySerializer
from rest_framework import permissions, routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication

class CompanyViewSet(viewsets.ModelViewSet):
    '''Api para consulta / creacion de compañias.'''
    authentication_classes = [OAuth2Authentication]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @list_route()
    def list(self, request):
        print(request.GET.get('filter'))
        data = Company.objects.filter(name__contains=request.GET.get('filter'))
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def create(self, request):
        print('create')
        print(request.data)
        return Response('Ok Create')

    def destroy(self,request):
        print('create')
        print(request.data)
        return Response('Ok Delete')

class CompanySearchViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
