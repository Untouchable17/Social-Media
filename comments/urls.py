from django.urls import path

from comments.views import CommentCreateView

app_name = 'comments'

urlpatterns = [
    path('create/<str:content_type>/<int:object_id>/', CommentCreateView.as_view(), name='comment-create')
]

