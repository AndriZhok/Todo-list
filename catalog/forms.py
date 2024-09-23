from django import forms

from catalog.models import Tag, Task


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "datetime", "optional_deadline", "tags"]
        widgets = {
            "datetime": forms.DateTimeInput(
                attrs={
                    "class": "form-control datetimepicker",
                    "placeholder": "Select date and time",
                }
            ),
            "optional_deadline": forms.DateTimeInput(
                attrs={
                    "class": "form-control datetimepicker",
                    "placeholder": "Select optional deadline",
                }
            ),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
