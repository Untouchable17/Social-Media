from rest_framework import serializers

from blog.models import Post, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)

    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.title')
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    body = serializers.CharField(required=True)
    photo = serializers.ImageField(required=True)
    created_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'category',
            'title',
            'slug',
            'body',
            'photo',
            'created_at',
            'tags'
        ]

