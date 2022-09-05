from dataclasses import fields
from django.forms import ModelForm
from .models import SampleAct

class SampleForm(SampleAct):
    class Meta:
        model = SampleAct
        fields = '__all__'