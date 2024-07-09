from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login

from django.contrib.auth import authenticate,login

from django.http.response import HttpResponse
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
        return redirect('login')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        users = authenticate(username=nome,password=senha)
        if users:
            auth_login(request,users)
            return render(request,'login.html', {'erro':f'Sucesso'})
        
        return render(request,'login.html', {'erro':f'Desculpe usuario não encontrado'})


def AddProdutos(request):
    if request.is_authenticated():
        return render(request, 'addprodutos.html')
    return redirect('cadastro')