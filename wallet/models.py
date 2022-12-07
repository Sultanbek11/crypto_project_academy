from uuid import uuid4
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Users


class Wallet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    summ_in_dollar = models.DecimalField(decimal_places=3, max_digits=40, null=True, default=0)
    wallets_token = models.UUIDField(default=uuid4)
    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = "Кошелёк"


class WalletValutes(models.Model):
    title_valute = models.CharField(max_length=60, null=True)
    owner = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_valute

    class Meta:
        verbose_name_plural = "Валюты в кошельке"


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchase')
    valuta = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.valuta

    class Meta:
        verbose_name_plural = "Покупки"


class PurchaseInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchase_info')

    def __str__(self):
        return self.token

    class Meta:
        verbose_name_plural = "Информация о пкупках"

@receiver(post_save, sender=Users)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(owner=instance)


@receiver(post_save, sender=Purchase)
def add_to_wallet(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.get(owner=instance.user)
        purchase_info = PurchaseInfo.objects.create(user=instance.user)
        purchase_info.save()
        if wallet.summ_in_dollar > 0 or None:
            wallet.summ_in_dollar += instance.amount
            wallet.save()
        else:
            wallet.summ_in_dollar = instance.amount
