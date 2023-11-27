from django.test import TestCase
from to_do.models import Todo, Tag


class TodoModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_todo_model_str_method(self):
        todo = Todo.objects.create(content="Test Task")
        todo.tag.set((self.tag,))
        todo.save()
        self.assertEqual(
            str(todo), f"{todo.content}, created: {todo.created}"
        )

    def test_tag_model_str_method(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), tag.name)
