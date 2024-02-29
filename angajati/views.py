from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AngajatiForm, SecondAngajatiForm
from .models import Angajat


class AngajatiCreateView(FormView):
    template_name = 'angajati/angajati_form.html'
    form_class = AngajatiForm
    success_url = reverse_lazy('angajati')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data

        Angajat.objects.create(
            nume=cleaned_data["nume"],
            varsta=cleaned_data["varsta"],
            cnp=cleaned_data["cnp"],
            telefon=cleaned_data["telefon"],
            mail=cleaned_data["mail"]
        )
        return result

    def form_invalid(self, form):
        print("Forma este invalida")
        return super().form_invalid(form)


class CreateAngajat(CreateView):
    template_name = 'angajati/create_angajati_usingbs.html'
    form_class = SecondAngajatiForm
    success_url = reverse_lazy('angajati')

#TemplateView
class AngajatDetailView(DetailView):
    template_name = 'angajati/angajat_detalii.html'
    model = Angajat


class AngajatUpdateView(UpdateView):
    template_name = 'angajati/angajati_form.html'
    model = Angajat
    form_class = SecondAngajatiForm
    success_url = reverse_lazy('angajati')


class AngajatDeleteView(DeleteView):
    template_name = 'angajati/delete_confirmation.html'
    model = Angajat
    success_url = reverse_lazy('angajati')