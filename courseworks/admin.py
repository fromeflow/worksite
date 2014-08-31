from django.contrib import admin
from courseworks.models import CourseWork


class CourseWorkAdmin(admin.ModelAdmin):
    def complete(self, request, queryset):
        queryset.update(completed=True)

    complete.short_description = "Пометить как сданную"

    list_display = ['title', 'student', 'academic_year', 'semester', 'completed']
    list_filter = ['year', 'completed']
    search_fields = ['title', 'student__surname']
    actions = [complete]


admin.site.register(CourseWork, CourseWorkAdmin)