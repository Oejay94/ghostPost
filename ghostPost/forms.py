from django import forms
from ghostPost.models import BoastRoast


class PostForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = [
            'title',
            'content',
            'boast_or_roast',
            'time'
        ]
