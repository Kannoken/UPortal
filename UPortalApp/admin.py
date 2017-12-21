from django.contrib import admin
from UPortalApp.models import *


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass


class AuthorPubAdmin(admin.TabularInline):
    extra = 0
    model = Author_of_publication


class FilePublicationsAdmin(admin.StackedInline):
    extra = 0
    model = Files_of_publication


class PublicationAdmin(admin.ModelAdmin):
    inlines = [AuthorPubAdmin, FilePublicationsAdmin, ]


class PlacePublicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Place_of_publication, PlacePublicationAdmin)
