from django.shortcuts import render
from .models import Produto
# Create your views here.
def pagina_inicial(request):

    #Armazenando na variável produtos, todos os objetos que foram resgatados do 
    produtos = Produto.objects.all()

    
    return render(request, 'home.html', {'produtos': produtos})