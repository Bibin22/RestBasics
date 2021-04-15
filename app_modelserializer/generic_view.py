from django.http import HttpResponse
from app_RestBasics.models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

class GenericAPIViews(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class GenericDetails(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)