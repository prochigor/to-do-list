from django.test import TestCase
from django.utils import timezone
from to_do.forms import TodoCreateForm, TaskSearchForm, TagSearchForm
from to_do.models import Tag


class TodoFormsTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_todo_create_form_valid(self):
        form_data = {
            "content": "Test Task",
            "deadline": timezone.now() + timezone.timedelta(days=1),
            "tag": [self.tag.id],
        }
        form = TodoCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_todo_create_form_invalid_deadline(self):
        form_data = {
            "content": "Test Task",
            "deadline": timezone.now() - timezone.timedelta(days=1),
            "tag": [self.tag.id],
        }
        form = TodoCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "Deadline can't be less than now", form.errors["deadline"]
        )

    def test_to_do_search_form(self):
        form_data = {"content": "Test Content"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_search_form(self):
        form_data = {"name": "Test Tag"}
        form = TagSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
