from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin
from .models import Post

class PostAdmin(ObjectPermissionsModelAdmin):
    pass

admin.site.register(Post, PostAdmin)