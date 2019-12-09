from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author_name', 'text', 'stars')

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    username= forms.CharField(max_length=20)
    password= forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password= forms.CharField(max_length=100, widget=forms.PasswordInput)
