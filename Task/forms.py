from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
        }


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['quiz_ref', 'num']
        widgets = {
            'question': forms.Textarea(),
            'is_ans_option_1': forms.CheckboxInput(attrs={'class': 'choice'}),
            'is_ans_option_2': forms.CheckboxInput(attrs={'class': 'choice'}),
            'is_ans_option_3': forms.CheckboxInput(attrs={'class': 'choice'}),
            'is_ans_option_4': forms.CheckboxInput(attrs={'class': 'choice'}),
            'description': forms.Textarea()
        }