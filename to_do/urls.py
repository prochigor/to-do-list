from django.urls import path

from to_do.views import (
    TodoListView,
    TOdoCreateView,
    TOdoUpdateView,
    TOdoDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_complete_task
)

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("todos/create/", TOdoCreateView.as_view(), name="to-do-create"),
    path(
        "todos/<int:pk>/update/",
        TOdoUpdateView.as_view(),
        name="to-do-update"
    ),
    path(
        "todos/<int:pk>/delete/",
        TOdoDeleteView.as_view(),
        name="to-do-delete"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "todos/<int:pk>/toggle-complete/",
        toggle_complete_task,
        name="toggle-complete",
    ),
]

app_name = "to_do"
