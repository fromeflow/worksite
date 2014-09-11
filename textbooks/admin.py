from django.contrib import admin

from textbooks.models import Author, Textbook, TextbookMaterial


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['surname', 'user']


admin.site.register(Author, AuthorAdmin)


class TextbookAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Textbook, TextbookAdmin)


class TextbookMaterialAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(TextbookMaterial, TextbookMaterialAdmin)