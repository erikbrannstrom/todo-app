from todo.models import List, Item
from django.contrib import admin

class ItemInline(admin.StackedInline):
    model = Item
    extra = 3

class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on')
    inlines = [ItemInline]

admin.site.register(List, ListAdmin)