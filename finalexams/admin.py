from django.contrib import admin

from finalexams.models import Finalexam


class FinalexamAdmin(admin.ModelAdmin):
    list_display = ['group', 'title']


admin.site.register(Finalexam, FinalexamAdmin)

