from django import forms
from .models import Post


class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control',
                'width': ''
            }
        )

    class Meta:
        model = Post
        fields = ['title', 'content', 'done', 'priority', 'due_date']

