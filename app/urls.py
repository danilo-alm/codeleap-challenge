from django.urls import path
from .views import PostListCreateView, PostDetailView, ReactView

urlpatterns = [
    path("post/", PostListCreateView.as_view(), name="post-list-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("react/", ReactView.as_view(), name="react-list-create"),
    path("react/<int:pk>/", ReactView.as_view(), name="react-detail"),
]