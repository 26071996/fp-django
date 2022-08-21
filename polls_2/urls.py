"""" Modulo para definicao de rotas do app"""
from django.urls import path
from.views import index, yury, carlos

#URLs config do app:
#Define a relacao entre um path e uma view
urlpatterns = [
   path('', index, name='index_polls_2'),

   #definir a url
   path('yury/', yury, name='yury_view'),
   path('carlos/', carlos, name='carlos_view'),
]
