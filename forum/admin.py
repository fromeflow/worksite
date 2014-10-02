from django.contrib import admin

from forum.models import Theme, Message


class ThemeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Theme, ThemeAdmin)


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)