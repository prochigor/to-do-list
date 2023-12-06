from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from to_do.models import Todo, Tag


class AdminPanelTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.todo = Todo.objects.create(content="Test Task")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admintestuser",
            password="admintestpass",
        )
        self.client.force_login(self.admin_user)

    def test_todo_admin_search(self):
        response = self.client.get(
            reverse("admin:to_do_todo_changelist"),
            {"q": "Test Task"}
        )
        self.assertContains(response, "Test Task")

    def test_tag_admin_search(self):
        response = self.client.get(
            reverse("admin:to_do_tag_changelist"),
            {"q": "Test Tag"}
        )
        self.assertContains(response, "Test Tag")

    def test_todo_list_view(self):
        response = self.client.get(reverse("to_do:index"))
        self.assertContains(response, "Test Task")

    def test_todo_create_view(self):
        response = self.client.post(
            reverse("to_do:to-do-create"),
            {"content": "New Task", "tag": self.tag.id}
        )
        self.assertEqual(response.status_code, 302)

    def test_todo_delete_view(self):
        response = self.client.post(
            reverse("to_do:to-do-delete", args=[self.todo.id])
        )
        self.assertEqual(response.status_code, 302)

    def test_tag_list_view(self):
        response = self.client.get(reverse("to_do:tag-list"))
        self.assertContains(response, "Test Tag")

    def test_tag_create_view(self):
        response = self.client.post(
            reverse("to_do:tag-create"), {"name": "New Tag"}
        )
        self.assertEqual(response.status_code, 302)

    def test_tag_update_view(self):
        response = self.client.post(
            reverse("to_do:tag-update", args=[self.tag.id]),
            {"name": "Updated Tag"}
        )
        self.assertEqual(response.status_code, 302)

    def test_tag_delete_view(self):
        response = self.client.post(
            reverse("to_do:tag-delete", args=[self.tag.id])
        )
        self.assertEqual(response.status_code, 302)
