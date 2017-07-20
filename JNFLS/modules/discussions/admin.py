from django.contrib import admin

from .models import DiscussionBoard, DiscussionPost, DiscussionReply


@admin.register(DiscussionBoard)
class DiscussionBoardAdmin(admin.ModelAdmin):
	list_display = ['name', 'type']


@admin.register(DiscussionPost)
class DiscussionPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'board', 'created', 'creator', 'is_anonymous']


@admin.register(DiscussionReply)
class DiscussionReplyAdmin(admin.ModelAdmin):
	list_display = ['post', 'created', 'creator', 'is_anonymous']
