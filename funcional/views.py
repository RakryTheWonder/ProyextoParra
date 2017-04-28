from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView


class Bienvenida(TemplateView):
    template_name = 'bienvenida.html'