from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Transaction, Wallet


@receiver(post_save, sender=Transaction)
def update_balance(sender, instance, **kwargs):
    wallet = instance.wallet
    if instance.type == 'Списать':
        if wallet.balance - instance.amount < 0:
            instance.status = 'Отклонено'
        else:
            wallet.balance -= instance.amount
            instance.status = 'Успешно'
    else:
        wallet.balance += instance.amount
        instance.status = 'Успешно'
    wallet.save()

