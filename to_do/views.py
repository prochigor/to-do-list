from django.urls import reverse_lazy
from django.views import generic

from to_do.models import Tag, Todo


class TodoListView(generic.ListView):
    model = Todo
    queryset = Todo.objects.all()
    template_name = "to_do/index.html"
    ordering = ["-created"]
    paginate_by = 5


class TOdoCreateView(generic.CreateView):
    model = Todo
    fields = ["content", "deadline", "tag"]
    success_url = reverse_lazy("to_do:index")


class TOdoUpdateView(generic.UpdateView):
    model = Todo
    fields = ["content", "is_done", "deadline", "tag"]
    success_url = reverse_lazy("to_do:index")


class TOdoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy("to_do:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
    queryset = Tag.objects.all()
    fields = "__all__"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tag-list")
