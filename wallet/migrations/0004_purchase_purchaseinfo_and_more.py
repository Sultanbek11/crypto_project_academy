# Generated by Django 4.1.3 on 2022-12-07 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0003_alter_wallet_summ_in_dollar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuta', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Покупки',
            },
        ),
        migrations.CreateModel(
            name='PurchaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('token', models.UUIDField(default=uuid.uuid4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Информация о пкупках',
            },
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='history_transactions',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='wallet',
            options={'verbose_name_plural': 'Кошелёк'},
        ),
        migrations.AlterModelOptions(
            name='walletvalutes',
            options={'verbose_name_plural': 'Валюты в кошельке'},
        ),
        migrations.AddField(
            model_name='wallet',
            name='wallets_token',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]
