from django import forms
from .models import Editor
from ckeditor.widgets import CKEditorWidget


class EditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget, label='Text editor')

    class Meta:
        model = Editor
        fields = '__all__'
