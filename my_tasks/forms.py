from django import forms
from .models import Post


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

    class Meta:
        model = Post
        fields = ["title", "content", "done", "priority", "due_date"]
