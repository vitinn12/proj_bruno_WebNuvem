from django.shortcuts import render, redirect
from .models import Produto

# Create your views here.
def index (request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")

        # salva direto no banco
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco)

        return redirect("index")  # recarrega a página

    # lista produtos
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})
