from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

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

class Vocab(models.Model):
	wordType= models.ForeignKey(WordType)
	level= models.ForeignKey(Level)
	text = models.CharField(max_length=200)
	definition = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	otherForm = models.CharField(max_length=50, blank=True, default="")

	def __unicode__(self):
		return self.text

class Passage(models.Model):
	level= models.ForeignKey(Level)
	title = models.CharField(max_length=200, default = "")
	text = HTMLField(default="add content")
	vocabs = models.ManyToManyField(Vocab)
	topics = models.ManyToManyField(Topic)
	
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
	topics = models.ForeignKey(Topic)
	passage = models.ForeignKey(Passage)
	video = models.ForeignKey(Video)
	text = models.TextField(default = "unknown")
	explanation = models.TextField
	vocabs = models.ManyToManyField(Vocab)
	
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	text = models.TextField
	value = models.BooleanField

	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

