from django.contrib import admin

from account.models import Album, Photo, User


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class PhotoAdmin(admin.ModelAdmin):
    pass
