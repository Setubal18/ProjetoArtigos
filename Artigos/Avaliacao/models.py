from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, blank=False, null=False)
    email = models.CharField('Email', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome


class Avaliador(Pessoa):
    curriculo = models.TextField()

    class Meta:
        verbose_name_plural = "Avaliadores"


# class Criterios(models.Model):


class Autor(Pessoa):
    # artigos = models.ManyToManyField(Artigo)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField('Titulo', max_length=50, blank=False, null=False)
    resumo = models.TextField()
    palavra_chave = models.CharField('Palavras Chaves', max_length=30, blank=False, null=False)
    autor = models.ManyToManyField(Autor)

    class Meta:
        verbose_name_plural = "Artigos"
    def __str__(self):
        return self.titulo

4


class Avaliacao(models.Model):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.CASCADE, default='')
    Quantidade_Tecnica = models.FloatField('Qualidade Tecnica',max_length=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    Inovacao = models.FloatField('Inovacao',max_length=2,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    Resultado = models.FloatField(max_length=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    Metodoliga = models.FloatField(max_length=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    AT = models.FloatField('Adequacao Tematica do Evento',max_length=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    Media = models.FloatField('Media',max_length=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    class Meta:
        verbose_name_plural = "Avaliacoes"

    def __str__(self):
        return self.artigo.titulo
