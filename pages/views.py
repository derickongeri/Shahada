from django.views import generic
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bio, SchoolInfo


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    context_object_name = 'all_bio'

    def get_queryset(self):
        return Bio.objects.all()


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class BioCreateView(CreateView):
    model = Bio
    template_name = 'pages/bio_form.html'
    fields = '__all__'


class SchoolInfoCreateView(CreateView):
    model = SchoolInfo
    template_name = 'pages/school_form.html'
    fields = '__all__'