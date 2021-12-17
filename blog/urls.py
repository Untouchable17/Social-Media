from django.urls import path
from users.views import register

from blog import views

urlpatterns = [
    path('', views.posts_list, name='posts_list_url'),
    path('user_contact/', views.user_contact, name='send_mail'),

    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', register, name="register"),

    path('post/create/', views.post_create,
         name="post_create_url"),
    path('post/<str:slug>/', views.PostDetailView.as_view(),
         name="post_detail_url"),
    path('post/<str:slug>/update/', views.PostUpdateView.as_view(),
         name="post_update_url"),
    path('post/<str:slug>/delete/', views.PostDeleteView.as_view(),
         name="post_delete_url"),

    path('post/<int:pk>/like', views.AddLike.as_view(),
         name="like"),
    path('post/<int:pk>/dislike', views.AddDisLike.as_view(),
         name="dislike"),

    path('tags/', views.tags_list, name="tags_list_url"),
    path('tag/<str:slug>/', views.TagDetailView.as_view(),
         name="tag_detail_url"),



]