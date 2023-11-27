from django.urls import path

from to_do.views import (
    TodoListView,
    TOdoCreateView,
    TOdoUpdateView,
    TOdoDeleteView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("todos/create", TOdoCreateView.as_view(), name="to-do-create"),
    path(
        "todos/<int:pk>/update",
        TOdoUpdateView.as_view(),
        name="to-do-update"
    ),
    path(
        "todos/<int:pk>/delete",
        TOdoDeleteView.as_view(),
        name="to-do-delete"
    ),
]

app_name = "to_do"
