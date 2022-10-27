from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class CustomLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            translation.activate(request.user.user_profile.language)
            request.LANGUAGE_CODE = request.user.user_profile.language