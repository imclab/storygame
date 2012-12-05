from django import forms
from storygame.stories.models import Line

class LineForm(forms.ModelForm):
    class Meta:
    	fields = ('line',)
        model = Line
