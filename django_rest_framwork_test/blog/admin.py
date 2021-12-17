from django.contrib import admin

from .models import Entry, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass
