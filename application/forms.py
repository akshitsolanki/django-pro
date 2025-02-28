from django import forms
from .models import ApplicationForm

class ApplicationFormForm(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields = ['name', 'email', 'message']
