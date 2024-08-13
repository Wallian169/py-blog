from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import index, PostDetailView

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "blog"
