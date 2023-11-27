from django.test import TestCase, Client
from django.urls import reverse
from to_do.models import Todo, Tag


class ToDoViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(name="Test Tag")
        self.todo = Todo.objects.create(content="Test Task")
        self.todo.tag.set((self.tag,))

    def test_todo_list_view(self):
        response = self.client.get(reverse("to_do:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        todos = Todo.objects.count()
        self.assertEqual(todos, 1)

    def test_todo_create_view(self):
        response = self.client.post(
            reverse("to_do:to-do-create"),
            {"content": "New Task", "tag": self.tag.id}
        )
        self.assertEqual(
            response.status_code, 302
        )
        todos = Todo.objects.count()
        self.assertEqual(todos, 2)

    def test_todo_update_view(self):
        response = self.client.post(
            reverse("to_do:to-do-update", args=[self.todo.id]),
            {"content": "Updated Task"},
        )
        self.assertEqual(
            response.status_code, 200
        )

    def test_todo_delete_view(self):
        response = self.client.post(
            reverse("to_do:to-do-delete", args=[self.todo.id])
        )
        self.assertEqual(
            response.status_code, 302
        )
        todos = Todo.objects.count()
        self.assertEqual(todos, 0)

    def test_tag_list_view(self):
        response = self.client.get(reverse("to_do:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tag")
        tag = Tag.objects.count()
        self.assertEqual(tag, 1)

    def test_tag_create_view(self):
        response = self.client.post(
            reverse("to_do:tag-create"), {"name": "New Tag"}
        )
        self.assertEqual(
            response.status_code, 302
        )
        tag = Tag.objects.count()
        self.assertEqual(tag, 2)

    def test_tag_update_view(self):
        response = self.client.post(
            reverse("to_do:tag-update", args=[self.tag.id]),
            {"name": "Updated Tag"}
        )
        self.assertEqual(
            response.status_code, 302
        )

    def test_tag_delete_view(self):
        response = self.client.post(
            reverse("to_do:tag-delete", args=[self.tag.id])
        )
        self.assertEqual(
            response.status_code, 302
        )
        tag = Tag.objects.count()
        self.assertEqual(tag, 0)

    def test_toggle_complete_task_view(self):
        response = self.client.get(
            reverse("to_do:toggle-complete", args=[self.todo.id])
        )
        self.assertEqual(
            response.status_code, 302
        )

        updated_todo = Todo.objects.get(id=self.todo.id)
        self.assertTrue(
            updated_todo.is_done
        )

    def test_todo_list_view_with_search(self):
        response = self.client.get(reverse("to_do:index"),
                                   {"content": "Test Task"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_tag_list_view_with_search(self):
        response = self.client.get(
            reverse("to_do:tag-list"), {"name": "Test Tag"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tag")
