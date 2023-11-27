from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Todo(models.Model):
    content = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="todos")
