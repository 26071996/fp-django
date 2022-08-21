from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#Existem dois tipos de Views
# sempre vai receber um parametro chamado Request signature: (request: Objeto)  -> retorna como Httpresponse
def index(request):
    return HttpResponse('<h1>Hola</h1>')


def yury(request):
    return HttpResponse('<h1>Yury solicitou</h1>')


def carlos(request):
    name = "Jaime"
    return render(request=request, template_name='index.html', context={'name': name})


