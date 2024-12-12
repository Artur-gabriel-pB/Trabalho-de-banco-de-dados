from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_conta, name='criar_conta'),
    path('consulta/<str:numero_conta>/', views.consultar_saldo, name='consultar_saldo'),
    path('deposito/', views.depositar, name='depositar'),
    path('saque/', views.sacar, name='sacar'),
    path('encerrar/', views.encerrar_conta, name='encerrar_conta'),
]

