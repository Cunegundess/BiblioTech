# Generated by Django 4.2.6 on 2023-11-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_filtro'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='nome',
            field=models.CharField(default='NomeEmprestimo', max_length=100, null=True),
        ),
    ]
