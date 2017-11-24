# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Paciente(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    data_nascimento = models.DateField(max_length=255, default='', verbose_name='Data Nascimento')
    adress = models.CharField(max_length=100, verbose_name='Endereço')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    cep = models.CharField(max_length=50, verbose_name='Cep')
    phone = models.CharField(max_length=20, verbose_name='Telefone', blank=True, null=True)
    mobile = models.CharField(max_length=20, verbose_name='Celular', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)

    def __str__ (self):
        return self.name


class Medico(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    data_nascimento = models.CharField(max_length=255, default= '',verbose_name='Data Nascimento', blank=True, null=True)
    adress = models.CharField(max_length=100, verbose_name='Endereço')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    cep = models.CharField(max_length=50, verbose_name='Cep')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    mobile = models.CharField(max_length=20, verbose_name='Celular')
    email = models.EmailField(verbose_name='Email')
    specialty = models.TextField(max_length=30, verbose_name='especialidade')
    #about_pathology = models.TextField(max_length=255, verbose_name='Sobre a patologia')

class Consulta(models.Model):
    doctor = models.ForeignKey(Medico, verbose_name='Medico responsavel')
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente a ser consultado')
    about_pathology = models.TextField(max_length=255, verbose_name='Sobre a patologia')


#models.ForeignKey
