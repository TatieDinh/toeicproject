from django.shortcuts import render
from .models import Topic, Vocab
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
	"""The home page for Toeic"""
	return render(request, 'Toeic/index.html')

def tests(request):
	"""Show all tests"""
	tests = Test.objects.order_by('date_added')
	context = {'tests': tests}
	return render(request, 'Toeic/tests.html', context)

def topics(request):
	"""Show all tests"""
	topics = Topic.objects.order_by('text')
	context = {'topics':topics}
	return render(request, 'Toeic/topics.html', context)

def topic(request, topic_id):
	"""show a single topic and all its vocabs"""
	topic = Topic.objects.get(id=topic_id)
	vocabs = topic.vocab_set.all()
	context = {'topic': topic, 'vocabs':vocabs}
	return render(request, 'Toeic/topic.html', context)

def checkvocab(request, topic_id): 
	topic = Topic.objects.get(id=topic_id)
	vocabs = topic.vocab_set.all()
	context = {'topic': topic, 'vocabs':vocabs}
	return render(request, 'Toeic/checkvocab.html', context)

def logout_view(request): 
	logout(request)
	return HttpResponseRedirect(reverse('Toeic:index'))

def register(request): 
	"""Register a new user.""" 
	if request.method != 'POST':
		form = UserCreationForm() 
	else: 
		form = UserCreationForm(data = request.POST)

	if form.is_valid():
		new_user = form.save()
		authenticated_user = authenticate(username=new_user.username, password=request.POST['password1']) 
		login(request, authenticated_user) 
		return HttpResponseRedirect(reverse('Toeic:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context) 
 
