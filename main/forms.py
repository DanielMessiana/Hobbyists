from django import forms

class QuestioneOne(forms.Form):
	Inside = forms.BooleanField(required=False)
	Outside = forms.BooleanField(required=False)
	Either = forms.BooleanField(required=False)

class QuestionsTwo(forms.Form):
	Free = forms.BooleanField(required=False)
	