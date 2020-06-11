from django import forms
from main.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }