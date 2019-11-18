from django import forms

from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ("title","text",)
