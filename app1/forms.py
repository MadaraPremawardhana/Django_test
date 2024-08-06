from django import forms
from app1.models import LogMessage

class LogForm(forms.ModelForm):
    class Meta:
        model = LogMessage  # this is the class from models.py
        fields = ("title", "message",)   # NOTE: the trailing comma is required
