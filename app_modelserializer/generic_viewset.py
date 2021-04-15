from .serializers import ArticleSerializer
from app_RestBasics.models import Article
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

class ArticleGenericViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
