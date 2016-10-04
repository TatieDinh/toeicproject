"""Define URL patterns for Toeic"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views
urlpatterns = [
	#homepage
	url(r'^$', views.index, name='index'),
	#show all tests.
	url(r'^tests/$', views.tests, name='tests'),
	url(r'^tests/(?P<test_id>\d+)/$', views.test, name='test'),
	url(r'^tests/result/(?P<test_id>\d+)/$', views.resulttest, name='resulttest'),
	url(r'^tests/resultvocabtest/(?P<test_id>\d+)/$', views.resultvocabtest, name='resultvocabtest'),
	url(r'^tests/checkvocabtest/(?P<test_id>\d+)/$', views.checkvocabtest, name='checkvocabtest'),
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	url(r'^topics/checkvocab/(?P<topic_id>\d+)/$', views.checkvocab, name='checkvocab'),
	url(r'^topics/resultvocab/(?P<topic_id>\d+)/$', views.resultvocab, name='resultvocab'),
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'), 
	url(r'^logout/$', views.logout_view, name='logout'), 
	url(r'^register/$', views.register, name='register'),
	url(r'^grammartopics/$', views.grammartopics, name='grammartopics'),
	url(r'^grammartopics/(?P<grammartopic_id>\d+)/$', views.grammartopic, name='grammartopic'),

	]



