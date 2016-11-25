from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    """Form used to input comments."""

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        """Initialize with the correct instance."""
        self.entry = kwargs.pop('entry')  # the blog entry instance
        super().__init__(*args, **kwargs)

    def save(self):
        comment = super().save(commit=False)
        comment.entry = self.entry
        comment.save()
        return comment
