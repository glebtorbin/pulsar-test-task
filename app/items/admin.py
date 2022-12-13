from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'price', 'image', 'status')
    list_editable = ('status',)
    search_fields = ('number',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
