from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date','name', 'email']
        widgets = {
            'date': forms.HiddenInput(),
        }