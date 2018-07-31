from django import forms
from adventure import models as a_models
class SafariForm(forms.ModelForm):

	class Meta:
		model = a_models.Safaris
		fields = ['place','category','description']