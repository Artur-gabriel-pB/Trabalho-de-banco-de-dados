
from django.shortcuts import render, redirect
from .models import Conta

def criar_conta(request):
    if request.method == "POST":
        numero = request.POST.get("numero")
        nome_cliente = request.POST.get("nome_cliente")
        saldo = request.POST.get("saldo", 0)

        if not Conta.objects.filter(numero=numero).exists():
            Conta.objects.create(numero=numero, nome_cliente=nome_cliente, saldo=saldo)
            return redirect('consulta_saldo')
        else:
            return render(request, 'criar_conta.html', {'erro': 'Número da conta já existe!'})

    return render(request, 'criar_conta.html')

def consultar_saldo(request, numero_conta):
    try:
        conta = Conta.objects.get(numero_conta=numero_conta)
        saldo = conta.saldo
    except Conta.DoesNotExist:
        saldo = None
    return render(request, 'contas/consultar_saldo.html', {'saldo': saldo})

from django.shortcuts import render
from .models import ContaBancaria  # Supondo que você tenha o modelo ContaBancaria

# Função para depositar



def saque(request):
    if request.method == "POST":
        numero = request.POST.get("numero")
        valor = float(request.POST.get("valor", 0))

        try:
            conta = Conta.objects.get(numero=numero)
            if valor <= conta.saldo:
                conta.saldo -= valor
                conta.save()
                return render(request, 'saque.html', {'conta': conta})
            else:
                return render(request, 'saque.html', {'erro': 'Saldo insuficiente!'})
        except Conta.DoesNotExist:
            return render(request, 'saque.html', {'erro': 'Conta não encontrada!'})

    return render(request, 'saque.html')

def encerrar_conta(request):
    if request.method == "POST":
        numero = request.POST.get("numero")

        try:
            conta = Conta.objects.get(numero=numero)
            if conta.saldo == 0:
                conta.delete()
                return render(request, 'encerrar_conta.html', {'mensagem': 'Conta encerrada com sucesso!'})
            else:
                return render(request, 'encerrar_conta.html', {'erro': 'Saldo não está zerado. Não é possível encerrar a conta.'})
        except Conta.DoesNotExist:
            return render(request, 'encerrar_conta.html', {'erro': 'Conta não encontrada!'})

    return render(request, 'encerrar_conta.html')

from django.shortcuts import render

# Função de view para a URL raiz
def home(request):
    return render(request, 'contas/criar_conta.html')  # Página que será renderizada


# Create your views here.
