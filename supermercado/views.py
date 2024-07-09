from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login

from django.http.response import HttpResponse
from .models import Produtos
# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        
        return render(request,'cadastro.html')
    else:
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        users = User.objects.filter(username=nome).first()
        if users:
            return render(request,'cadastro.html', {'erro':'Desculpe já exite um usuario com esse nome'})
        users = User.objects.create_user(username=nome,password=senha)
        users.save()
        auth_login(request,users)
        return redirect('addprod')
        

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        users = authenticate(username=nome,password=senha)
        if users:
            auth_login(request,users)
            return redirect('addprod')
        
        return render(request,'login.html', {'erro':f'Desculpe usuario não encontrado'})


def AddProdutos(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            
            
            return render(request, 'addprodutos.html')
        else:
            nome = request.POST.get('nome_prod')
            code = request.POST.get('code_prod')
            vali = request.POST.get('vali_prod')
            peso = request.POST.get('peso_prod')
            forn = request.POST.get('forn_prod')
            validacao = Produtos.objects.filter(nome_podu=nome).first()
            if validacao:
                return render(request, 'addprodutos.html',{'msg':'Desculpe item existente no sistema'})
            Produtos.objects.create(nome_podu=nome,cod_barras=int(code),valid=vali,
                                    peso=float(peso),fornecedor=forn)
            return render(request, 'addprodutos.html',{'msg':'Item adicionado com sucesso'})
            
    return redirect('cadastro')