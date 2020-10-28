from django import forms
from .models import Details

class upd_form(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"
