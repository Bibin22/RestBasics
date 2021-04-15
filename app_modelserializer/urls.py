from django.urls import path
from .views import article_list, article_detail
from .apiview import api_article_list, api_article_details

urlpatterns = [
    path('', article_list),
    path('detail/<int:id>', article_detail),
    path('api_list', api_article_list),
    path('api_details/<int:id>', api_article_details)

]