from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	"""docstring for Home"""
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)
class AboutPageView(TemplateView):
		"""docstring for AboutPageView"""
		def get(self, request, **kwargs):
			return render(request, 'about.html', context=None)
				