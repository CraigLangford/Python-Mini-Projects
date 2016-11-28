from django.test import TestCase
from django_webtest import WebTest
from django.contrib.auth import get_user_model
from django.template import Template, Context

from .forms import CommentForm
from .models import Entry, Comment


class EntryModelTest(TestCase):

    def test_string_representation(self):
        """ Ensure that the entry has a string representation """
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), "My entry title")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

    def test_get_absolute_url(self):
        user = get_user_model().objects.create(username='some_user')
        entry = Entry.objects.create(title="My entry title", author=user)
        self.assertIsNotNone(entry.get_absolute_url())


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class HomePageTests(TestCase):

    """ Test whether our blog post entries show up on the home page """

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_entry(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entries(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        Entry.objects.create(title='2-title', body='2-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')
        self.assertContains(response, '2-body')

    def test_no_entries(self):
        response = self.client.get('/')
        self.assertContains(response, 'No blog entries yet.')


class EntryViewTest(WebTest):

    def setUp(self):
        self.user = get_user_model().objects.create(username="some_user")
        self.entry = Entry.objects.create(title="1-title", body="1-body",
                                          author=self.user)

    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.body)

    def test_comments_below_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, "No comments yet.")

    def test_view_page(self):
        page = self.app.get(self.entry.get_absolute_url())
        self.assertEqual(len(page.forms), 1)

    def test_form_error(self):
        page = self.app.get(self.entry.get_absolute_url())
        page = page.form.submit()
        self.assertContains(page, "This field is required.")

    def test_form_success(self):
        page = self.app.get(self.entry.get_absolute_url())
        page.form['name'] = "Phillip"
        page.form['email'] = "phillip@example.com"
        page.form['body'] = "Test comment body."
        page = page.form.submit()
        self.assertRedirects(page, self.entry.get_absolute_url())


class CommentModelTest(TestCase):

    """ Tests the comments section of the blog page """
    
    def setUp(self):
        self.user = get_user_model().objects.create(username="some user")
        self.entry = Entry.objects.create(title="1-title", body="1-body",
                                          author=self.user)
        self.comment = Comment.objects.create(entry=self.entry,
                                              name='some_commenter',
                                              email="test@user.com",
                                              body="Comment text"
                                             )

    def test_string_representation(self):
        comment = Comment(body="My comment body")
        self.assertEqual(str(comment), "My comment body")

    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.comment.body)

class CommentFormTest(TestCase):

    """Used for testing user comments on blog posts."""

    def setUp(self):
        """Set up comment form"""
        user = get_user_model().objects.create_user('zoidberg')
        self.entry = Entry.objects.create(title="1-title", body="1-body",
                                          author=user)

    def test_init(self):
        """Ensure comment form accepts a entry keyword argument."""
        CommentForm(entry=self.entry)

    def test_init_without_entry(self):
        """Want to make sure an error is raised if no entry created."""
        with self.assertRaises(KeyError):
            CommentForm()

    def test_valid_data(self):
        """Tests if form is valid with correct data."""
        form = CommentForm({
            'name': "Commenter Name",
            'email': "commenter@name.com",
            'body': "Hi there!",
        }, entry=self.entry)
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.name, "Commenter Name")
        self.assertEqual(comment.email, "commenter@name.com")
        self.assertEqual(comment.body, "Hi there!")
        self.assertEqual(comment.entry, self.entry)

    def test_blank_data(self):
        """Tests form with no data input."""
        form = CommentForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'email': ['This field is required.'],
            'body': ['This field is required.'],
        })

class EntryHistoryTagTest(TestCase):
    
    TEMPLATE = Template("{% load blog_tags %} {% entry_history %}")

    def setUp(self):
        self.user = get_user_model().objects.create(username='zoidberg')

    def test_entry_shows_up(self):
        entry = Entry.objects.create(author=self.user, title="My entry title")
        rendered = self.TEMPLATE.render(Context())
        self.assertIn(entry.title, rendered)
