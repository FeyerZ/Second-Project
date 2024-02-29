
from django import forms
from .models import Angajat

class AngajatiForm(forms.Form):
    nume = forms.CharField(max_length=100)
    varsta = forms.IntegerField(min_value=1, max_value=50)
    cnp = forms.CharField(max_length=13)
    telefon = forms.CharField(max_length=20)
    mail = forms.EmailField(max_length=50)


class SecondAngajatiForm(forms.ModelForm):
    class Meta:
        model = Angajat
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visile_fields in self.visible_fields():
            visile_fields.field.widget.attrs['class'] = 'form-control'


