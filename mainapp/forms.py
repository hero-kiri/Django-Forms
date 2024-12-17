from django import forms
from .models import Post

# Вариант 1
class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    is_published = forms.BooleanField(required=False)
    category = forms.ChoiceField(choices=[
        ('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3')
        ])
    
# Вариант 2
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'content': forms.Textarea()
        }