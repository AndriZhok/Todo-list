from django import forms

from catalog.models import Tag


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
