from django.contrib import admin

from textbooks.models import Textbook, TextbookMaterial


class TextbookAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Textbook, TextbookAdmin)


class TextbookMaterialAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(TextbookMaterial, TextbookMaterialAdmin)