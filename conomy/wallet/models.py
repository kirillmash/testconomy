from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    class Type(models.TextChoices):
        ADD = 'Пополнить'
        SUBTRACT = 'Списать'

    type = models.CharField(max_length=20, choices=Type.choices, default=Type.ADD)

    class Status(models.TextChoices):
        PAYED = 'Успешно'
        IN_PROCESSING = 'В обработке'
        DECLINED = 'Отклонено'
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.IN_PROCESSING)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"Транзакция №{self.pk} на сумму {self.amount}"
