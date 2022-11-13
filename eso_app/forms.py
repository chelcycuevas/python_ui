from django import forms
from .models import BuildEditor


class BuildEditorForm(forms.ModelForm):
    class Meta:
        model = BuildEditor
        fields = "__all__"
