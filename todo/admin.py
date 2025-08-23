from django.contrib import admin
from .models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "created_at",
        "deadline",
        "is_done",
        "display_tags"
    )
    list_filter = ("is_done", "created_at", "deadline", "tags")
    search_fields = ("content",)
    filter_horizontal = ("tags",)  # правильне поле ManyToMany
    ordering = ("-created_at",)

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    display_tags.short_description = "Tags"

    def mark_done(self, request, queryset):
        updated = queryset.update(is_done=True)
        self.message_user(request, f"{updated} task(s) marked as done.")
    mark_done.short_description = "Mark selected tasks as done"
