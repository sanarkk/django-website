from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def index(request):
    return render(request, "test.html", {})


class Home(TemplateView):
    template_name = 'test.html'