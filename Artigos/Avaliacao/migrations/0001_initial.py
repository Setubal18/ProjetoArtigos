# Generated by Django 2.0.2 on 2018-04-10 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('resumo', models.TextField()),
                ('palavra_chave', models.CharField(max_length=30, verbose_name='Palavras Chaves')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantidade_Tecnica', models.FloatField(max_length=6, verbose_name='QualidadeTecnica')),
                ('Inovacao', models.FloatField(max_length=6, verbose_name='Inovacao')),
                ('Resultado', models.FloatField(max_length=6)),
                ('Metodoliga', models.FloatField(max_length=6)),
                ('AT', models.FloatField(max_length=6, verbose_name='AdequacaoTematicadoEvento')),
                ('Media', models.FloatField(max_length=6, verbose_name='Media')),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Avaliacao.Artigo')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Avaliacao.Pessoa')),
            ],
            bases=('Avaliacao.pessoa',),
        ),
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Avaliacao.Pessoa')),
                ('curriculo', models.TextField()),
            ],
            bases=('Avaliacao.pessoa',),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='avaliador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Avaliacao.Avaliador'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='autor',
            field=models.ManyToManyField(to='Avaliacao.Autor'),
        ),
    ]
