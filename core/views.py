from django.shortcuts import render, redirect
from .models import Produto

# Create your views here.
def index (request):
    return render (request, 'index.html')


def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        if nome and preco:
            try:
                Produto.objects.create(nome=nome, preco=preco)
            except Exception as e:
                print("Erro ao criar produto:", e)
        return redirect('home')
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})
