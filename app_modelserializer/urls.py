from django.urls import path, include
from .views import article_list, article_detail
from .apiview import api_article_list, api_article_details
from .class_views import ArticleAPIView, ArticlesDetails
from .generic_view import GenericAPIViews, GenericDetails
from .authentications import GenericAPIView
from .viewsets import ArticleViewset
from .generic_viewset import ArticleGenericViewset
from .model_viewset import ArticleModelViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('viewset', ArticleViewset, basename='article')
router.register('generic_viewset', ArticleGenericViewset, basename='article')
router.register('model_viewset', ArticleModelViewSet, basename='article')
urlpatterns = [
    path('', article_list),
    path('detail/<int:id>', article_detail),
    path('api_list', api_article_list),
    path('api_details/<int:id>', api_article_details),
    path('api_class_list', ArticleAPIView.as_view()),
    path('api_class_details/<int:id>', ArticlesDetails.as_view()),
    path('generic_list', GenericAPIViews.as_view()),
    path('generic_details/<int:id>', GenericDetails.as_view()),
    path('auth_view', GenericAPIView.as_view()),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('generic_viewset/',include(router.urls)),
    path('generic_viewset/<int:pk>', include(router.urls)),
    path('model_viewset/',include(router.urls)),
    path('model_viewset/<int:pk>', include(router.urls)),


]