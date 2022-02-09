from django.contrib import admin
from .models import Post


class AdminImages(admin.ModelAdmin):
    list_display = ['photo', 'title', 'content']

admin.site.register(Post)