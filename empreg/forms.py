from django import forms
from empreg.models import Emp
class Empform(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"
