from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from Toeic.models import Type, WordType, Level, Test, Topic, Vocab, Passage, Video, Question, Answer
# Audio, 
admin.site.register(Type)
admin.site.register(WordType)
admin.site.register(Level)
admin.site.register(Test)
admin.site.register(Topic)
admin.site.register(Vocab)
admin.site.register(Passage)
admin.site.register(Video)
# admin.site.register(Audio)
admin.site.register(Question)
admin.site.register(Answer)
