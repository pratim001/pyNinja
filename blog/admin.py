from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','catagory','publish','created','updated')
    list_filter = ('catagory','author','publish','created')
    search_fields = ('title','body','author')
    raw_id_fields = ('author',)
    prepopulated_fields = {'slug':('title',)}
