from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin
from .models import Post, Comment

class PostAdmin(ObjectPermissionsModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)