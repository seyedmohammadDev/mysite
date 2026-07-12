from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','created_date',"counted_views","published_date" ,"created_date","status", )
    list_filter = ("status",)
    empty_value_display = '-empty-'
    ordering = ('created_date',)
    search_fields = ['title' , 'content']
admin.site.register(Post,PostAdmin)
