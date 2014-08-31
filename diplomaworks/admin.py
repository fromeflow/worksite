from django.contrib import admin
from diplomaworks.models import DiplomaWork


class DiplomaWorkAdmin(admin.ModelAdmin):
    def complete(self, request, queryset):
        queryset.update(completed=True)

    complete.short_description = "Пометить как сданную"

    list_display = ['title', 'student', 'academic_year', 'completed']
    list_filter = ['year', 'completed']
    search_fields = ['title', 'student__surname']
    actions = [complete]


admin.site.register(DiplomaWork, DiplomaWorkAdmin)