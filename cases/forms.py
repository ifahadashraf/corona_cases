from django import forms
from cases.models import Case


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'name',
            'nic',
            'age',
            'city',
            'address',
            'travel_history',
        ]
