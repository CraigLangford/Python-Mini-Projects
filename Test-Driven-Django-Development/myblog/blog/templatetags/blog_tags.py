from ..models import Entry

from django import template

register = template.Library()

@register.inclusion_tag('blog/_entry_history.html')
def entry_history():
    entries = Entry.objects.all()[:5]
    return {'entries': entries}
