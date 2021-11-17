from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def TituloEvento(request, titulo_evento):
    consulta = Evento.objects.get(titulo=titulo_evento)
    #response = Evento.objects.get(Evento.descricao)
    return HttpResponse('<h1>Por enquanto é isso {}</h1>'.format(consulta))
    #return object.descricao

def lista_eventos(request, id):
    evento = Evento.objects.get(id=id)
    response = {'evento':evento}
    return render(request, 'agenda.html', response)