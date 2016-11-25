from django.db import models
from django.core.urlresolvers import reverse


class Entry(models.Model):

    """ Model for blog entry """

    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def get_absolute_url(self):
        return reverse('entry_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"


class Comment(models.Model):

    """ Model for comment section of blog """

    entry = models.ForeignKey(Entry)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.body
