from django import forms
from main.models import Profile

class Update(forms.ModelForm):
	class Meta:
		model = Profile

		fields=[
			"location",
			"image",
		]