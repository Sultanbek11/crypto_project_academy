# Generated by Django 4.1.3 on 2022-12-03 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valuta', '0008_remove_value_valut_value_title'),
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='count_valutes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='valuta.value'),
        ),
    ]
