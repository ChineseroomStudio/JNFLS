"""JNFLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from JNFLS.modules.accounts import views as accounts_views
from JNFLS.modules.boards import views as boards_views
from JNFLS.modules.broadcasts import views as broadcasts_views
from JNFLS.modules.classes import views as classes_views
from JNFLS.modules.clubs import views as clubs_views
from JNFLS.modules.discussions import views as discussions_views
from JNFLS.modules.dorms import views as dorms_views
from JNFLS.modules.quantification import views as quantification_views
from JNFLS.modules.sports import views as sports_views


urlpatterns = [
	# Account URL start
	url(r'^$', accounts_views.home_view, name='home'),
	url(r'^login/$', accounts_views.login_view, name='login'),
	url(r'^logout/$', accounts_views.logout_view, name='logout'),
	url(r'^register/$', accounts_views.register_view, name='register'),
	# Account URL end

	# Board URL start
	url(r'^school/posts/$', boards_views.school_post_board_view, name='school-post-board'),
	url(r'^school/post/new/$', boards_views.school_post_new_view, name='school-post-new'),
	url(r'^school/post/(?P<post_id>[0-9]*)/$', boards_views.post_article_view, name='school-post-article'),
	url(r'^school/post/(?P<post_id>[0-9]*)/edit/$', boards_views.post_article_view, name='school-post-edit'),
	url(r'^school/post/(?P<post_id>[0-9]*)/delete/$', boards_views.post_article_view, name='school-post-delete'),

	# url(r'^class/(?P<class_id>[0-9]*)/post/new/$', boards_views.class_post_board_view, name='class-post-new'),
	# url(r'^class/(?P<class_id>[0-9]*)/post/(?P<post_id>[0-9]*)/$', boards_views.post_article_view, name='class-post-article'),
	# url(r'^class/(?P<class_id>[0-9]*)/post/(?P<post_id>[0-9]*)/edit/$', boards_views.class_post_board_view, name='class-post-edit'),
	# url(r'^class/(?P<class_id>[0-9]*)/post/(?P<post_id>[0-9]*)/delete/$', boards_views.class_post_board_view, name='class-post-article'),
	#
	# url(r'^club/(?P<club_id>[0-9]*)/post/new/$', boards_views.class_post_board_view, name='club-post-new'),
	# url(r'^club/(?P<club_id>[0-9]*)/post/(?P<post_id>[0-9]*)$', boards_views.class_post_board_view, name='club-post-article'),
	# url(r'^club/(?P<club_id>[0-9]*)/post/(?P<post_id>[0-9]*)/edit/$', boards_views.class_post_board_view, name='club-post-edit'),
	# url(r'^club/(?P<club_id>[0-9]*)/post/(?P<post_id>[0-9]*)/delete/$', boards_views.class_post_board_view, name='club-post-delete'),
	# # Board URL end
	#
	# # Broadcast URL start
	# url(r'^broadcast/passed/$', broadcasts_views.school_discussion_board_view, name='broadcast-passed'),
	# url(r'^broadcast/all/$', broadcasts_views.school_discussion_board_view, name='broadcast-all'),
	# url(r'^broadcast/new/$', broadcasts_views.school_discussion_board_view, name='broadcast-new'),
	# url(r'^broadcast/(?P<broadcast_id>[0-9]*)/pass/$', broadcasts_views.school_discussion_board_view, name='broadcast-pass'),
	# url(r'^broadcast/(?P<broadcast_id>[0-9]*)/deny/$', broadcasts_views.school_discussion_board_view, name='broadcast-deny'),
	# # Broadcast URL end
	#
	# # Class URL start
	# url(r'^class/(?P<class_id>[0-9]*)/$', classes_views.school_discussion_board_view, name='class-home'),
	# # Class URL end
	#
	# # Club URL start
	# url(r'^club/new/apply/$', clubs_views.school_discussion_board_view, name='new-club-apply'),
	# url(r'^club/new/(?P<club_id>[0-9]*)/$', clubs_views.school_discussion_board_view, name='new-club-application'),
	# url(r'^club/new/pass/$', clubs_views.school_discussion_board_view, name='new-club-pass'),
	# url(r'^club/new/deny/$', clubs_views.school_discussion_board_view, name='new-club-deny'),
	#
	# url(r'^club/(?P<club_id>[0-9]*)/$', clubs_views.school_discussion_board_view, name='club-home'),
	# # Club URL end
	#
	# # Discussion URL start
	# url(r'^school/discussion/$', discussions_views.school_discussion_board_view, name='school-discussion-board'),
	# url(r'^school/discussion/new/$', discussions_views.school_discussion_board_view, name='school-discussion-new'),
	# url(r'^school/discussion/(?P<discussion_id>[0-9]*)/reply/$', discussions_views.school_discussion_board_view, name='school-discussion-reply-to-discussion'),
	# url(r'^school/discussion/(?P<discussion_id>[0-9]*)/reply/(?P<reply_id>[0-9]*)$', discussions_views.school_discussion_board_view, name='school-discussion-reply-to-reply'),
	# url(r'^school/discussion/(?P<discussion_id>[0-9]*)/delete/$', discussions_views.school_discussion_board_view, name='school-discussion-delete'),
	#
	# url(r'^class/(?P<class_id>[0-9]*)/discussion/$', discussions_views.school_discussion_board_view, name='class-discussion-board'),
	# url(r'^class/(?P<class_id>[0-9]*)/discussion/new/$', discussions_views.school_discussion_board_view, name='class-discussion-new'),
	# url(r'^class/(?P<class_id>[0-9]*)/discussion/(?P<discussion_id>[0-9]*)/reply/$', discussions_views.school_discussion_board_view, name='class-discussion-reply-to-discussion'),
	# url(r'^class/(?P<class_id>[0-9]*)/discussion/(?P<discussion_id>[0-9]*)/reply/(?P<reply_id>[0-9]*)$', discussions_views.school_discussion_board_view, name='class-discussion-reply-to-reply'),
	# url(r'^class/(?P<class_id>[0-9]*)/discussion/(?P<discussion_id>[0-9]*)/delete/$', discussions_views.school_discussion_board_view, name='class-discussion-delete'),
	#
	# url(r'^club/(?P<club_id>[0-9]*)/discussion/$', discussions_views.school_discussion_board_view, name='club-discussion-board'),
	# url(r'^club/(?P<club_id>[0-9]*)/discussion/new$', discussions_views.school_discussion_board_view, name='club-discussion-new'),
	# url(r'^club/(?P<club_id>[0-9]*)/discussion/(?P<discussion_id>[0-9]*)/reply/$', discussions_views.school_discussion_board_view, name='club-discussion-reply-to-discussion'),
	# url(r'^club/(?P<club_id>[0-9]*)/discussion/(?P<discussion_id>[0-9]*)/reply/(?P<reply_id>[0-9]*)$', discussions_views.school_discussion_board_view, name='club-discussion-reply-to-reply'),
	# url(r'^club/(?P<club_id>[0-9]*)/discussion/(?P<discussion_id>[0-9]*)/delete/$', discussions_views.school_discussion_board_view, name='club-discussion-delete'),
	# # Discussion URL end
	#
	# # Dorm URL start
	# # Dorm URL end
	#
	# # Quantification URL start
	# # Quantification URL end
	#
	# # Sport URL start
	# url(r'^sport/(?P<class_id>[0-9]*)/(?P<user_id>[0-9]*)/$', sports_views.school_discussion_board_view, name='sport-game-control'),
	# # Sport URL end

	# Admin URL start
	url(r'^admin/', admin.site.urls),
	# Admin URL end

]
