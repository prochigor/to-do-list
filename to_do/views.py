from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from to_do.forms import TodoCreateForm, TaskSearchForm, TagSearchForm
from to_do.models import Tag, Todo


class TodoListView(generic.ListView):
    model = Todo
    template_name = "to_do/index.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        content = self.request.GET.get("content", "")
        context["search_form"] = TaskSearchForm(initial={"content": content})
        return context

    def get_queryset(self):
        queryset = Todo.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(content__icontains=form.cleaned_data["content"])
        return queryset


class TOdoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoCreateForm
    success_url = reverse_lazy("to_do:index")


class TOdoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoCreateForm
    success_url = reverse_lazy("to_do:index")


class TOdoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy("to_do:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
    fields = "__all__"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TagSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Tag.objects.all()
        form = TagSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


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


def toggle_complete_task(request, pk):
    task = Todo.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do:index"))
