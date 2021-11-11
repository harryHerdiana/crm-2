from django.contrib import admin
from .models import Post,Author,Tag,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter = ("tag","author")
    list_display = ("title","author")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name","post")

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)