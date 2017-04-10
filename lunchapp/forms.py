from django import forms
from django.contrib.auth.models import User
from lunchapp.models import Comment, Topic


__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "LGPLv3.0"
__version__ = "0.0.1"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    tos_agreement = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'lg-checkbox'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-field'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-field',
                'placeholder': 'email@example.com'
            }),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-field'})
        }


class TopicForm(forms.ModelForm):
    """
    Form used to create new Topic.
    """
    class Meta:
        model = Topic
        fields = {'name', 'text'}
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Topic name',
                'class': 'form-control form-field',
                'id': 'new-topic-name'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Comment',
                'class': 'form-control form-field',
                'id': 'new-topic-text'
            })
        }


class CommentForm(forms.ModelForm):
    """
    Form used to create new Comment.
    Pass Topic ID as part of the URL.
    """
    class Meta:
        model = Comment
        fields = {'text'}
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Comment',
                'id': 'new-comment-text'
            })
        }

