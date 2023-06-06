from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<slug:slug>', UpdatePostView.as_view(), name="update_post"),
    path('article/<slug:slug>/remove', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<slug:slug>', LikeView, name='like_post'),
    path('article/<slug:slug>/comment/', AddCommentView.as_view(), name="add_comment"),
]