from django import forms
from .models import BinaryTree


class BinaryTreeNodeForm(forms.ModelForm):
    class Meta:
        model = BinaryTree
        fields = ['name', 'parent', 'is_left', 'is_right']




