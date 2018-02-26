from django import forms
from .models import Charge


class SearchForm(forms.Form):
    charge = forms.ModelChoiceField(
        queryset = Charge.objects, label='料金', required=False)