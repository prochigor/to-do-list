from django.contrib import admin

from to_do.models import Tag, Todo


@admin.register(Todo)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("tag__name", "deadline", "is_done")


@admin.register(Tag)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name",)
