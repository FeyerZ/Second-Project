from django.shortcuts import render
from store.models import Order
from angajati.models import Angajat


# Create your views here.

def home(request):
    angajati_din_db_values = Angajat.objects.all()
    template = 'home/index.html'  # second_project/templates/home/index.html
    template_data_model = {
        'angajati_din_db': angajati_din_db_values
    }
    return render(request, template, context=template_data_model)


def angajati_view(request):
    angajati_din_db_values = Angajat.objects.all()
    template_data_model = {
        'angajati_din_db': angajati_din_db_values
    }
    return render(request, 'angajati/angajati.html', context=template_data_model)


def angajati_total_count(request):
    lista_angajati = Angajat.objects.all()
    numar_angajati = lista_angajati.count()

    context = {
        'lista_angajati':lista_angajati,
        'numar_angajati':numar_angajati
    }

    return render(request, 'home/angajati_count.html', context=context)


def angajati_pestesub20(request):
    lista_angajati = Angajat.objects.all()

    return render(request, 'home/angajati_pestesub20.html', context=lista_angajati)