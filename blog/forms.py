from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # ordering = '-pk'  # 여기도 아니라면 도대체 어디인가...
        fields = ('content',)
