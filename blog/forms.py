from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)

class CommentForm(forms.Form):
    author = forms.CharField(label='Your nick:', max_length=200)
    text = forms.CharField(label='Put your comment here:',widget=forms.Textarea)