from django.contrib import admin
from .models import Faculty, Chair, Employee, Specialty

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Faculty, FacultyAdmin)


class ChairAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty']

admin.site.register(Chair, ChairAdmin)


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    list_filter = ['standard_generation', 'type']

admin.site.register(Specialty, SpecialtyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'chair', 'position']
    search_fields = ['surname']

admin.site.register(Employee, EmployeeAdmin)