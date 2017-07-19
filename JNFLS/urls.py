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

from JNFLS.modules.accounts import views as accounts_view

urlpatterns = [
	# Account URL start
	url(r'^$', accounts_view.home_view, name='home'),
	url(r'^login/$', accounts_view.login_view, name='login'),
	url(r'^logout/$', accounts_view.logout_view, name='logout'),
	url(r'^register/$', accounts_view.register_view, name='register'),

	# Account URL end

	# Admin URL start
	url(r'^admin/', admin.site.urls),
	# Admin URL end

]
