from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here


class OrderView(LoginRequiredMixin, TemplateView):
    template_name = "food_order/make_order.html"


    login_url = "/login/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})