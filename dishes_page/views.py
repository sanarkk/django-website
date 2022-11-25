from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Dish


# Create your views here


class DishesView(LoginRequiredMixin, TemplateView):
    template_name = "dishes_page/dishes.html"

    login_url = "/"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(DishesView, self).get_context_data(**kwargs)
        context['dishes'] = Dish.objects.all()
        return context
