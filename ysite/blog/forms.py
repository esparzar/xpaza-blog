from django import forms

from .models import Post


class MyForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('tittle', 'text',)