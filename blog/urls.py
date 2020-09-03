
from django.contrib import admin
from django.urls import path
from blog.views import ArticleListView,ArticleDetailsView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView


urlpatterns = [

path('' , ArticleListView.as_view()  , name="article-list"),
path('<int:id>/' , ArticleDetailsView.as_view()  , name="article-details"),
path('create/' , ArticleCreateView.as_view()  , name="article-create"),
path('<int:id>/update/' , ArticleUpdateView.as_view()  , name="article-update"),
path('<int:id>/delete/' , ArticleDeleteView.as_view()  , name="article-delete"),


]