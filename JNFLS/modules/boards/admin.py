from django.contrib import admin

from .models import Post, PostBoard


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']


class PostBoardAdmin(admin.ModelAdmin):
	list_display = ['name', 'type', 'my_class', 'my_club']


admin.site.register(PostBoard, PostBoardAdmin)
admin.site.register(Post, PostAdmin)
