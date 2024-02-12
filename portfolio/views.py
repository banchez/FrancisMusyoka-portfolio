from django.http import HttpResponse
from django.template import loader


# Create your views here.
def portfolio(request):
  return HttpResponse("My name is francis")


def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
