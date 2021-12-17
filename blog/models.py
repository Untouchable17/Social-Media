from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Имя категории")
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="blogs", blank=True)
    title = models.CharField(max_length=150, db_index=True, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    body = models.TextField(blank=True, db_index=True, verbose_name="Контент блога")
    photo = models.ImageField(upload_to="photos/", blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    replace_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    is_published = models.BooleanField(default=True, verbose_name="Общий доступ")
    comments = GenericRelation('comments.Comment')
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    dislikes = models.ManyToManyField(User, blank=True, related_name="dislikes")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']


class Tag(models.Model):

    title = models.CharField(max_length=50, verbose_name="Тэг")
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
