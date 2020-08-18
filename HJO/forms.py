from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',  'first_name',
                  'last_name', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'title', 'author', 'tag', 'post',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'name', 'email')

class TestForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('pic', 'position', 'name', 'testimony')
