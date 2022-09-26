from django.contrib import admin

from account.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
