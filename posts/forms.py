from django import forms
from .models import Post, Comment


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'summary', 'image', 'content', 'categories', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        exclude = ['name']
