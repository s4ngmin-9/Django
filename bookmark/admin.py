from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    list_display_links =  ['name','url']
    list_filter = ['name','url']

#admin.site.register(Bookmark,BookmarkAdmin)