from django import forms
from report.models import Comment, Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['week', 'category', 'comment_body']

class EditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['week', 'category', 'comment_body']