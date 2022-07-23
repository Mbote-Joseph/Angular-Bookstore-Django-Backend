from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('get', views.getBook, name='get'),
    path('post', views.postBook, name='post'),
    path('put/<int:pk>', views.putBook, name='put'),
    path('delete/<int:pk>', views.deleteBook, name='delete'),
]