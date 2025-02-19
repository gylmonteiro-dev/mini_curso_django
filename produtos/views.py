from django.shortcuts import render,redirect, get_object_or_404
from .models import Produto
# Create your views here.
def pagina_inicial(request):

    #Armazenando na variável produtos, todos os objetos que foram resgatados do 
    produtos = Produto.objects.all()

    
    return render(request, 'home.html', {'produtos': produtos})

def cadastrar_produto(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        imagem = request.FILES.get('imagem')

        Produto.objects.create(titulo=titulo, descricao=descricao, preco=preco, imagem=imagem)
        return redirect("pagina-inicial")
    return render(request, "cadastra_produto.html")


def detalhar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    print(produto)
    return render(request, 'detalhes_produto.html')
