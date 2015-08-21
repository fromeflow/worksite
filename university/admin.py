from django.contrib import admin
from .models import Faculty, Chair, Employee

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Faculty, FacultyAdmin)


class ChairAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty']

admin.site.register(Chair, ChairAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'chair', 'position']
    search_fields = ['surname']

admin.site.register(Employee, EmployeeAdmin)