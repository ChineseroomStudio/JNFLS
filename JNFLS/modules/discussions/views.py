from django.shortcuts import render

from .models import DiscussionBoard, DiscussionReply, DiscussionPost


def school_discussion_board_view(request):
	if request.method == 'GET':
		discussion_board = DiscussionBoard.objects.get(type=0)
		discussions = discussion_board.posts.order_by('created')
		return render(request, 'views/discussion-board.html', {'discussions': discussions})
	elif request.method == 'POST':
		pass

