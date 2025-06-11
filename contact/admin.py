from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'firstName', 'lastName', 'phone', 'show',
    ordering = '-id',
    search_fields = 'id', 'firstName', 'lastName'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'firstName', 'lastName', 'show'
    list_display_links = 'id', 'phone'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
 