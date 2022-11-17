# Generated by Django 4.1.3 on 2022-11-17 13:59

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='age',
        ),
        migrations.RemoveField(
            model_name='users',
            name='login',
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=phone_field.models.PhoneField(default=1, max_length=31, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]