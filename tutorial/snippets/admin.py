from django.contrib import admin
#from tutorial import snippets
from .models import Snippet

#admin.site.register(Snippet)
@admin.register(Snippet)
class snippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language')

# Register your models here.
