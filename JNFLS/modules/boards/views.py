from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404

from .models import PostBoard, Post
from .forms import NewPostForm


@login_required
def school_post_board_view(request):
	if request.method == 'GET':
		school_post_board = PostBoard.objects.get(type=0)
		school_posts = school_post_board.posts.order_by('updated')
		return render(request, 'views/post-board.html', {'posts': school_posts})


@login_required
@permission_required('boards.school_post' , raise_exception=True)
def school_post_new_view(request):
	if request.method == 'GET':
		data = {'headbar_title'   : '校园公告',
		        'headbar_subtitle': '校园管理', }
		return render(request, 'views/new-post.html', data)
	elif request.method == 'POST':
		form = NewPostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['title']

			school_post_board = PostBoard.objects.get(type=0)
			new_post = Post(title=title, content=content, board_id=school_post_board.id)
			new_post.save()
			return redirect('school-post-article', post_id=new_post.id)
		else:
			return redirect('school-post-new')


@login_required
def class_post_board_view(request):
	school_class = request.user.my_schoolclass
	print(school_class)
	if school_class:
		class_post_board = school_class.post_board
		class_posts = class_post_board.posts.order_by('updated')
		return render(request, 'views/post-board.html', {'posts': class_posts})
	else:
		raise Http404


@login_required
def club_post_board_view(request, id):
	if request.method == 'GET':
		club_post_board = get_object_or_404(PostBoard, id=id)
		club_posts = club_post_board.posts.order_by('updated')
		return render(request, 'views/post-board.html', {'posts': club_posts})


@login_required
def post_article_view(request, id):
	post = get_object_or_404(Post, id=id)
	post.views += 1
	post.save()
	return render(request, 'views/article.html', {'post': post})
