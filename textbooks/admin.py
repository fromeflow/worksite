from django.contrib import admin

from textbooks.models import Textbook, TextbookFile


class TextbookAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Textbook, TextbookAdmin)


class TextbookFileAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(TextbookFile, TextbookFileAdmin)
