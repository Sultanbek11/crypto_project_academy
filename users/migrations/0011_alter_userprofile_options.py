# Generated by Django 4.1.3 on 2022-12-02 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_users_verify_cod_users_verify_code_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Профиль Пользователя', 'verbose_name_plural': 'Профили Пользователей'},
        ),
    ]
