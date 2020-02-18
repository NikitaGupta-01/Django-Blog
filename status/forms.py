from django import forms
from .models import Status

class StatusForms(forms.ModelForm):
	class Meta:
		models	= Status
		fields	=['user','content']
		
	def clean(self,*args,**kwargs):
		data	= self.cleaned_data
		content	= data.get('content',None)
		if(content == ""):
			raise forms.ValidationError('Content not entered')
		return super().clean(*args,**kwargs)