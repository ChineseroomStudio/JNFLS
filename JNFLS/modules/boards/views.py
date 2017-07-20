from django.shortcuts import render, get_object_or_404

from .models import PostBoard, Post


def school_post_board_view(request):
	if request.method == 'GET':
		school_postboard = PostBoard.objects.get(type=0)
		school_posts = school_postboard.posts.order_by('updated')
		return render(request, 'views/postboard.html', {'posts': school_posts})


def class_post_board_view(request, id):
	return render(request, 'views/postboard.html')


def club_post_board_view(request, id):
	return render(request, 'views/postboard.html')


def post_article_view(request, id):
	post = get_object_or_404(Post, id=id)
	post.views += 1
	post.save()
	return render(request, 'views/article.html', {'post': post})
