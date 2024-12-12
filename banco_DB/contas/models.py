from django.db import models

class Conta(models.Model):
    numero_conta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Conta {self.numero_conta} - Saldo: {self.saldo}"


# Create your models here.
