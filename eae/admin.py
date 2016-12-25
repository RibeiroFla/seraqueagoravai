from django.contrib import admin
from eae.models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class ShelfAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Shelf,ShelfAdmin)
