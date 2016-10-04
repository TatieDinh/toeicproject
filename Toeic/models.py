from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class WordType(models.Model):
	"""type of the exercise"""
	text = models.CharField(max_length=100, default="")
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class Type(models.Model):
	"""type of the exercise"""
	text = models.CharField(max_length=100, default="")
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text


class Level(models.Model):
	text = models.CharField(max_length=50, default="")
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.text 

class Test(models.Model):
	level= models.ForeignKey(Level)
	text = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text 

class Topic(models.Model):
	text = models.CharField(max_length=200, default="")
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class GrammarTopic(models.Model):
	level= models.ForeignKey(Level)
	title = models.CharField(max_length=200, default="")
	text = HTMLField(default="add content")
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Vocab(models.Model):
	wordType= models.ForeignKey(WordType)
	level= models.ForeignKey(Level)
	text = models.CharField(max_length=200)
	definition = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	otherForm = models.CharField(max_length=50, blank=True, default="")
	topic = models.ManyToManyField(Topic)

	def __unicode__(self):
		return self.text

class Passage(models.Model):
	level= models.ForeignKey(Level)
	title = models.CharField(max_length=200, default = "")
	text = HTMLField(default="add content")
	vocabs = models.ManyToManyField(Vocab)
	topics = models.ManyToManyField(Topic)
	isTestSix = models.BooleanField(default=False)
	
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Video(models.Model):
	level= models.ForeignKey(Level)
	title = models.CharField(max_length=200, default = "")
	text = models.TextField(default="")
	url = models.URLField(null=True)
	vocabs = models.ManyToManyField(Vocab)
	topics = models.ManyToManyField(Topic)

	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

# class Audio(models.Model):
	# text = models.CharField(max_length=200, default = "")
	# audio = models.FileField(upload_to=None, max_length=100)
	# video= models.ForeignKey(Video)

class Question(models.Model):
	level= models.ForeignKey(Level)
	typeOf = models.ForeignKey(Type)
	topics = models.ManyToManyField(Topic)
	grammarTopics = models.ManyToManyField(GrammarTopic)
	passage = models.ForeignKey(Passage)
	video = models.ForeignKey(Video)
	text = models.TextField(default = "")
	fulltext = models.TextField(default = "")
	explanation = models.TextField(default = "")
	translation = models.TextField(default = "")
	vocabs = models.ManyToManyField(Vocab)
	tests = models.ManyToManyField(Test)

	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	text = models.TextField(default="")
	isTrue = models.BooleanField(default = False)

	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class UserAnswer(models.Model):
	user = models.ForeignKey(User)
	test = models.ForeignKey(Test)
	question = models.ForeignKey(Question)
	answer = models.ForeignKey(Answer)

	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.answer

class UserVocab(models.Model):
	user = models.ForeignKey(User)
	vocab = models.ForeignKey(Vocab)
	text = models.TextField(default="")

	date_added = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.text

