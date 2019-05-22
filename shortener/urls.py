from django.urls import path, re_path
from .views import UrlShortener, viewUrl, CreateUrl
from . import views
from django.urls import include


urlpatterns = [
    path('',  UrlShortener.as_view(), name="index"),
    path('-/<slug:generated_link>', viewUrl, name="url-view" ),
    path('create_link',  CreateUrl.as_view(), name="create_url"),
    path('urls/', views.UrlListView.as_view(), name='urls'),
    path('url/<int:pk>', views.UrlDetailView.as_view(), name='url-detail')
]
