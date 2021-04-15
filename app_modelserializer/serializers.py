from rest_framework import serializers
from app_RestBasics.models import Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
