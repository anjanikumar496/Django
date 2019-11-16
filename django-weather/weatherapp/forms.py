from django.forms import ModelForm, TextInput
from .models import City
class City_Form(ModelForm):
	class Meta:
		model=City
		fields={'name'}
		widgets={
		'name': TextInput(attrs={'class':'input', 'placeholder':'enter city name'}),
		}

		