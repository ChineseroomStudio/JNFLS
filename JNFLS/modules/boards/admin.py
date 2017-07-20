from django.contrib import admin

from .models import Post, PostBoard


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']


@admin.register(PostBoard)
class PostBoardAdmin(admin.ModelAdmin):
	list_display = ['name', 'type', 'my_class', 'my_club']
