from django.contrib import admin

from .models import Category, Ticket


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket)
