from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def index(request):
    if request.method == "POST":
        # Cadastrar produto
        if "cadastrar" in request.POST:
            nome = request.POST.get("nome")
            preco = request.POST.get("preco")
            Produto.objects.create(nome=nome, preco=preco)
        elif "deletar" in request.POST:
            produto_id = request.POST.get("produto_id")
            produto = get_object_or_404(Produto, id=produto_id)
            produto.delete()
        return redirect("index")
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})
