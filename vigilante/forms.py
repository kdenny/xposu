from django import forms

from .models import Complaint, Store

class PostForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ('type', 'text')