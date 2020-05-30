from django.urls import path
from .views import (ArticleListView,ArticleDetailsView,ArticleUpdateView,ArticleDeleteView,ArticlaCreateView)

urlpatterns=[
    path('',ArticleListView.as_view(),name='article_list'),
    path('<int:pk>',ArticleDetailsView.as_view(),name='article_detail'),
    path('new/',ArticlaCreateView.as_view(),name='article_create'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
]