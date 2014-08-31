from django.contrib import admin
from courses.models import Chair, Course

admin.site.register(Chair)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'speciality', 'chair', 'closed']
    list_filter = ['speciality', 'chair']
    search_fields = ['title']

admin.site.register(Course, CourseAdmin)