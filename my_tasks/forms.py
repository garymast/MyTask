from django import forms
from .models import Post
from django.utils import timezone
from django.core.exceptions import ValidationError


class ItemForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["done"].widget.attrs["class"] = "form-control"
        self.fields["priority"].widget.attrs["class"] = "form-control"
        self.fields["due_date"].widget = forms.widgets.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        )


    def clean_due_date(self):
        data = self.cleaned_data['due_date']
        if data < timezone.now().date():
            print("Due date cannot be earlier than today.")
            raise forms.ValidationError("Due date cannot be earlier than today.")
        return data


    class Meta:
        model = Post
        fields = ["title", "content", "done", "priority", "due_date"]
