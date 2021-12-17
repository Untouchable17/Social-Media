from django.urls import path

from blog.api.api_views import (
    PostListCreateAPIView,
    CategoryListCreateAPIView,
    PostDetailAPIView,
    CategoryDetailAPIView
)

urlpatterns = [
    path('blogs/', PostListCreateAPIView.as_view(),
         name="blogs_list"),
    path('blogs/<str:id>', PostDetailAPIView.as_view(),
         name="blog_detail"),
    path('categories/', CategoryListCreateAPIView.as_view(),
         name="categories"),
    path('categories/<str:id>', CategoryDetailAPIView.as_view(),
         name="categories_detail"),

]

