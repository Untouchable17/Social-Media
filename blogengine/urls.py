from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from rest_framework.routers import SimpleRouter

from users import views as user_views
from users.views import ViewProfile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.api.urls')),
    path('chat/', include("chat.urls")),
    path('blog/', include('blog.urls')),
    path('captcha/', include('captcha.urls')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('profile/<int:pk>/', ViewProfile.as_view(), name="profile-detail"),
    path('profile/settings/', user_views.profile, name='profile_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

