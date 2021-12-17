from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from blog.api.serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class PostListCreateAPIView(ListCreateAPIView):

    serializer_class = PostSerializer
    pagination_class = CategoryPagination
    queryset = Post.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']


class PostDetailAPIView(RetrieveUpdateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'


class CategoryDetailAPIView(RetrieveUpdateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


class CategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = CategorySerializer

    queryset = Category.objects.all()


