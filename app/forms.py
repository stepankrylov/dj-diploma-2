from django.contrib.auth.models import User
from django import forms
from app.models import Review


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)


class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea, label='Имя')
    text = forms.CharField(widget=forms.Textarea, label='Содержание')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
