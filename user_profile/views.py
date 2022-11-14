from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from djangoauth.models import UserProfile
from django.views.generic.edit import UpdateView
from .forms import UpdateProfileForm  # Create your views here
from django.contrib.auth.models import User


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user_profile/user_profile.html"

    login_url = "/login/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = "user_profile/update_profile.html"
    form_class = UpdateProfileForm

    def get_form_kwargs(self):
        kwargs = super(UpdateProfile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    success_url = "/"
