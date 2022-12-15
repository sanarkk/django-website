from braces.views import LoginRequiredMixin
from django.views.generic import FormView
from .models import Checkout
from dishes_page.models import Dish
from .forms import CheckoutForm


# Create your views here


class OrderView(LoginRequiredMixin, FormView):
    template_name = "food_order/make_order.html"
    form_class = CheckoutForm
    success_url = "/order/"

    login_url = "/login/"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['dishes'] = Dish.objects.all()
        context['orders'] = Checkout.objects.all()
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #print "form is valid"
        return super(OrderView, self).form_valid(form)