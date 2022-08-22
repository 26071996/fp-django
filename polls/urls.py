from django.urls import path
from .views import primeira_view

## Temos que respeitar o nome urlspatterns
urlpatterns = [
    path('', primeira_view, name='first view')
]
