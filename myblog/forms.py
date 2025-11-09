from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','style':'max-width:600px'}),
            'body':forms.Textarea(attrs={'class':'form-control','rows':'5','style':'max-width:600px'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','body']
        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'請留言'}),
        }       