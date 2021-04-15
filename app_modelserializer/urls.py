from django.urls import path
from .views import article_list, article_detail
from .apiview import api_article_list, api_article_details
from .class_views import ArticleAPIView, ArticlesDetails
from .generic_view import GenericAPIViews, GenericDetails
urlpatterns = [
    path('', article_list),
    path('detail/<int:id>', article_detail),
    path('api_list', api_article_list),
    path('api_details/<int:id>', api_article_details),
    path('api_class_list', ArticleAPIView.as_view()),
    path('api_class_details/<int:id>', ArticlesDetails.as_view()),
    path('generic_list', GenericAPIViews.as_view()),
    path('generic_details/<int:id>', GenericDetails.as_view())

]