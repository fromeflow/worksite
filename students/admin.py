from django.contrib import admin
from students.models import Speciality, Group, Student


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    list_filter = ['standard_generation', 'type']


admin.site.register(Speciality, SpecialityAdmin)


class GroupAdmin(admin.ModelAdmin):
    def send_down(self, request, queryset):
        for group in queryset:
            Student.objects.filter(group=group).update(sent_down=True)

    send_down.short_description = 'Расформировать группу'

    list_display = ['name', 'speciality', 'years']
    list_filter = ['year', 'speciality']
    actions = [send_down]


admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    def send_down(self, request, queryset):
        queryset.update(sent_down=True)

    send_down.short_description = 'Отчислить студента'

    list_display = ['surname', 'name', 'patronymic', 'group', 'user']
    list_filter = ['group__year', 'group']
    search_fields = ['surname']
    actions = [send_down]


admin.site.register(Student, StudentAdmin)