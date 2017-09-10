# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import DadosPessoais


def curriculo_exibir(request):

	 pessoa = DadosPessoais.objects.all()
	 context = {'pessoa': pessoa}
	 return render(request, 'curriculios/curriculo_exibir.html', context)