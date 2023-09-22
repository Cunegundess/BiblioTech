# Generated by Django 4.2.5 on 2023-09-13 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(blank=True, max_length=50, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('data_falecimento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneroLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publicadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('is_funcionario', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('descricao', models.TextField()),
                ('ano_publicacao', models.IntegerField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(auto_now_add=True)),
                ('data_devolucao', models.DateField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_devolucao', models.DateField(auto_now_add=True)),
                ('multa', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('emprestimo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='API.emprestimo')),
            ],
        ),
        migrations.CreateModel(
            name='DetalhesLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades', models.PositiveIntegerField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.autor')),
                ('emprestimo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.emprestimo')),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.generolivro')),
                ('publicadora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.publicadora')),
            ],
        ),
    ]