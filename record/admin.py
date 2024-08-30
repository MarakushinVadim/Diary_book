from django.contrib import admin

from record.models import Record


@admin.register(Record)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "created_at",
    )
    search_fields = ("name", "author", "id")
    list_filter = ("created_at", "name", "author")
