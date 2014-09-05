from django.contrib import admin

from seminars.models import Seminar, SeminarFile


class SeminarAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']


admin.site.register(Seminar, SeminarAdmin)


class SeminarMaterialsAdmin(admin.ModelAdmin):
    list_display = ['seminar', 'title', 'file']


admin.site.register(SeminarFile, SeminarMaterialsAdmin)
