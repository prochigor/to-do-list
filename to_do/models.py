from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Todo(models.Model):
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="todos")
