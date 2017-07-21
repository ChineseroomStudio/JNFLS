from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import PostBoard, Post


def school_post_board_view(request):
	if request.method == 'GET':
		school_postboard = PostBoard.objects.get(type=0)
		school_posts = school_postboard.posts.order_by('updated')
		return render(request, 'views/postboard.html', {'posts': school_posts})

def school_post_new_view(request):
	if request.method == 'POST':
		pass


def class_post_board_view(request):
	school_class = request.user.my_schoolclass
	print(school_class)
	if school_class:
		class_postboard = school_class.post_board
		class_posts = class_postboard.posts.order_by('updated')
		return render(request, 'views/postboard.html', {'posts': class_posts})
	else:
		raise Http404


def club_post_board_view(request, id):
	if request.method == 'GET':
		club_postboard = get_object_or_404(PostBoard, id=id)
		club_posts = club_postboard.posts.order_by('updated')
		return render(request, 'views/postboard.html', {'posts': club_posts})


def post_article_view(request, id):
	post = get_object_or_404(Post, id=id)
	post.views += 1
	post.save()
	return render(request, 'views/article.html', {'post': post})
