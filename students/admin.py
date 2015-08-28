from django.contrib import admin
from .models import Group, Student


class GroupAdmin(admin.ModelAdmin):
    def send_down(self, request, queryset):
        for group in queryset:
            Student.objects.filter(group=group).update(sent_down=True)

    send_down.short_description = 'Расформировать группу'

    list_display = ['name', 'specialty', 'years']
    list_filter = ['entrance_year', 'specialty']
    actions = [send_down]


admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    def send_down(self, request, queryset):
        queryset.update(sent_down=True)

    send_down.short_description = 'Отчислить студента'

    list_display = ['surname', 'name', 'patronymic', 'group', 'user']
    list_filter = ['group__entrance_year', 'group']
    search_fields = ['surname']
    actions = [send_down]


admin.site.register(Student, StudentAdmin)