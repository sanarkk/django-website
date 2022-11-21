from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here


class DishesView(LoginRequiredMixin, TemplateView):
    template_name = "dishes_page/dishes.html"

    login_url = "/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})
