# Generated by Django 4.2.6 on 2023-11-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_emprestimo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(),
        ),
    ]