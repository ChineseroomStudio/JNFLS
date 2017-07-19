from django.contrib import admin

from .models import DiscussionBoard, DiscussionPost, DiscussionReply


class DiscussionBoardAdmin(admin.ModelAdmin):
	list_display = ['name', 'type']


class DiscussionPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'board', 'created', 'creator', 'is_anonymous']


class DiscussionReplyAdmin(admin.ModelAdmin):
	list_display = ['post', 'created', 'creator', 'is_anonymous']


admin.site.register(DiscussionBoard, DiscussionBoardAdmin)
admin.site.register(DiscussionPost, DiscussionPostAdmin)
admin.site.register(DiscussionReply, DiscussionReplyAdmin)