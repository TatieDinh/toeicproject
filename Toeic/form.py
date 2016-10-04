from django import forms

from .models import UserVocab, Answer, Question, UserAnswer

class UserVocabForm(forms.Form):

	text = forms.CharField(label='Answer', max_length=100)

	# def __init__(self, vocab_id, user_id):
	# 	super(UserVocabForm, self).__init__()
	# 	self.fields['user'] = user_id
	# 	self.fields['vocab'] = vocab_id


class UserAnswerForm(forms.Form):
	answer = forms.ModelChoiceField(queryset=Answer.objects.none())

	def __init__(self, question_id, *args, **kwargs):
		super(UserAnswerForm, self).__init__(*args, **kwargs)
		self.fields['answer'].queryset = Answer.objects.filter(question=question_id)