from django.forms import ModelForm
from . models import groupMessage


class chatModelForm(ModelForm):
    class Meta:
        model = groupMessage
        fields = ['body']
        