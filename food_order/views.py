from braces.views import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Checkout
from dishes_page.models import Dish
from .forms import CheckoutForm


# Create your views here


class OrderView(LoginRequiredMixin, CreateView):
    model = Checkout
    template_name = "food_order/make_order.html"
    form_class = CheckoutForm
    success_url = "/order/"

    login_url = "/login/"
    raise_exception = True

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(OrderView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context["dishes"] = Dish.objects.all()
        context["orders"] = Checkout.objects.all()
        return context
