from django.contrib import admin

from .models import Follow, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Follow)
