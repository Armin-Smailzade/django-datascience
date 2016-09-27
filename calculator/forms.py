from django import forms

# Importing from models - Using Model as the Form
# from .models import SignUp
from .models import Breast_Variables

class BreastForm(forms.ModelForm):

	race = forms.ChoiceField(
				widget = forms.Select(
					attrs={
	                'class': 'form-control',
	                'placeholder': 'Name goes here',
	            	}), 
                choices = ([('1','White'), ('2','Black'),]), 
                initial='3', 
                required = True,
                help_text='100 characters max.'
                )

	vitalStatusRecord = forms.ChoiceField(
				widget = forms.Select(
					attrs={
	                'class': 'form-control',
	                'placeholder': 'Name goes here',
	            }), 
                choices = ([('1','Alive'), ('2','Dead'),]), 
                initial='3', 
                required = True,
                )

	grade = forms.ChoiceField(
				widget = forms.Select(
					attrs={
	                'class': 'form-control',
	                'placeholder': 'Name goes here',
	            }), 
                choices = ([('1','1'), ('2','2'),('3','3'), ('4','4'),('5','5'), ('6','6'),('7','7'), ('8','8'), ('9','9'),]), 
                initial='3', 
                required = True,
                )

	maritalStatus = forms.ChoiceField(
				widget = forms.Select(
					attrs={
	                'class': 'form-control',
	                'placeholder': 'Name goes here',
	            }), 
                choices = ([('1','Single'), ('2','Married'),]), 
                initial='3', 
                required = True,
                )

	histologicType = forms.CharField(
				widget=forms.TextInput(
	            	attrs={
	                'class': 'form-control',
	                'placeholder': 'Name goes here',
	                'type' : 'text'
	            	}),
				required = True,
				error_messages={'required': 'Please enter Histologic Type.'},
				)

	behaviorCode = forms.ChoiceField(
				widget = forms.Select(
					attrs={
	                'class': 'form-control',
	                'placeholder': 'Name goes here',
	            	}), 
                choices = ([('1','Single'), ('2','Married'),('3','3'), ('4','4'),]), 
                initial='3', 
                required = True,
                )

	csExtension = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }),
				required = True,

				)

	csLymphNode = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }),
				required = True,
				)

	radiation = forms.ChoiceField(
				widget = forms.Select(
					attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
	            	}), 
                choices = ([('1','1'), ('2','2'),('3','3'), ('4','4'),('5','5'), ('6','6'),('7','7'), ('8','8'), ('9','9'),]), 
                initial='3', 
                required = True,
                )

	seerHistoricStageA = forms.ChoiceField(
				widget = forms.Select(
					attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
	            	}), 
                choices = ([('1','1'), ('2','2'),('3','3'), ('4','4'),('5','5'), ('6','6'),('7','7'), ('8','8'), ('9','9'),]), 
                initial='3', 
                required = True,
                )

	ageAtDiognosis = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }),
				required = True,
				)

	csTumorSize = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }))

	regionalNodesPositive = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }),
				required = True,
				)

	regionalNodesExamined = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }),
				required = True,
				)

	survivalMonths = forms.CharField(
				widget=forms.TextInput(
		            attrs={
		                'class': 'form-control',
		                'placeholder': 'Name goes here',
		                'type' : 'text'
		            }))

	class Meta:
		model = Breast_Variables
		exclude = ('id',)

	def set_result(self, value):
		data = self.data.copy()
		data['result'] = value 
		self.data = data

class CommentForm(forms.Form):

    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
























# SAMPLE
# class SignUpForm(forms.ModelForm):

# 	class Meta:
# 		model = SignUp
#		fields = (....)