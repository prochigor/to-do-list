from django.urls import reverse_lazy
from django.views import generic

from to_do.models import Tag, Todo


class TodoListView(generic.ListView):
    model = Todo
    template_name = "to_do/index.html"
    ordering = ["-created"]
    paginate_by = 10


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
