from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.
#def index(request):
#    return redirect('/agenda/')

def TituloEvento(request, titulo_evento):
    consulta = Evento.objects.get(titulo=titulo_evento)
    response = {'evento':consulta}
    return HttpResponse('<h1>{consulta.descricao}</h1>'.format(response))
    #return object.descricao

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)