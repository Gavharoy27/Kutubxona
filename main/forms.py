from django import forms
from .models import *

class TalabaForm(forms.Form):
    ism = forms.CharField(max_length = 50)
    kurs = forms.IntegerField(max_value = 4, min_value = 1)
    guruh = forms.CharField(max_length = 20)
    kitob_soni = forms.IntegerField(min_value = 0)

class MuallifForm(forms.Form):
    ism = forms.CharField(max_length = 50)
    jins = forms.CharField()
    t_sana = forms.DateField()
    kitob_soni = forms.IntegerField(min_value = 0)
    tirik = forms.BooleanField()

class KitobModelForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'

class RecordModelForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class KutubxonachiForm(forms.Form):
    ISH_VAQTI_CHOICES = (
        ('08:00-13_00', '08:00-13_00'),
        ('13:00-18:00', '13:00-18:00'),
        ('18:00-23:00', '18:00-23:00')
    )
    ism = forms.CharField(max_length = 50)
    ish_vaqti = forms.ChoiceField(choices = ISH_VAQTI_CHOICES)
