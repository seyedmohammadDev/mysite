from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
admin.site.register(Post,PostAdmin)
