from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ManifestModel
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = "pages/manifest_home.html"
    model = ManifestModel

class ManifestListView(ListView):
    template_name = "pages/manifest_list.html"
    model = ManifestModel
    context_object_name = 'manifested_goals'

class ManifestDetailView(DetailView):
    template_name = 'pages/detail_manifest.html'
    model = ManifestModel


class ManifestCreateView(CreateView):
    template_name = 'pages/create_manifest.html'
    model = ManifestModel
    fields = ['goal', 'description', 'image_url', 'dreamer']


class ManifestUpdateView(UpdateView):
    template_name = 'pages/update_manifest.html'
    model = ManifestModel
    fields = ['goal', 'description', 'image_url', 'dreamer']


class ManifestDeleteView(DeleteView):
    template_name = 'pages/delete_manifest.html'
    model = ManifestModel
    success_url = reverse_lazy('manifest_list')