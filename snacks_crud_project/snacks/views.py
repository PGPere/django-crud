from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snacks
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class SnacksList(ListView):
    template_name = "snacks_list.html"
    model = Snacks
    context_object_name = 'sn_list'


class SnacksDetail(DetailView):
    template_name = "snacks_detail.html"
    model = Snacks


class SnacksCreateView(CreateView):
    template_name = 'snacks-create.html'
    model = Snacks
    fields = ['name', 'description', 'purchaser']


class SnacksUpdateView(UpdateView):
    template_name = 'snacks-update.html'
    model = Snacks
    fields = ['name', 'description', 'purchaser']


class SnacksDeleteView(DeleteView):
    template_name = 'snacks-delete.html'
    model = Snacks
    success_url = reverse_lazy('snacks_list')
