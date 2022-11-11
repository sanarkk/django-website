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
            'request': self.request.user,
        })
        return kwargs

    def form_valid(self, form):
        form_up = UpdateProfileForm
        if form_up.is_valid(form):
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User()
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return user


    # fields = [
    #    'first_name',
    #    'last_name',
    #    #'avatar',
    #    #'phone_number',
    # ]

    success_url = "/"
