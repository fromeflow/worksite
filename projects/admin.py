from django.contrib import admin
from .models import CourseProject, FinalProject


class ProjectAdmin(admin.ModelAdmin):
    def complete(self, request, queryset):
        queryset.update(completed=True)

    complete.short_description = "Пометить как сданную"

    search_fields = ['title', 'student__surname']
    actions = [complete]


class CourseProjectAdmin(ProjectAdmin):
    list_display = ['title', 'student']

admin.site.register(CourseProject, CourseProjectAdmin)


class FinalProjectAdmin(ProjectAdmin):
    list_display = ['title', 'student', 'defence_year']

admin.site.register(FinalProject, FinalProjectAdmin)