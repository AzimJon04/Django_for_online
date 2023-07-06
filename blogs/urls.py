from django.urls import path

from .views import HomePages, ListBlog, DetailBlog, BlogCreate, BlogUpdate, BlogDelete


urlpatterns = [
    path('', HomePages, name='home'),
    path('blogs/', ListBlog.as_view(), name='list_blog'),
    path('create_blog/', BlogCreate.as_view(), name='create_blog'),
    path('blogs/<int:pk>/', DetailBlog.as_view(), name='detail_blog'),
    path('blogs/<int:pk>/update/', BlogUpdate.as_view(), name='update_blog'),
    path('blogs/<int:pk>/delete/', BlogDelete.as_view(), name='delete_blog'),
]
