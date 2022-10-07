from datetime import datetime

import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


# Create your views here.
class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPI(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        print(password)

        user = User.objects.filter(email=email).first()

        if not email:
            raise AuthenticationFailed("failed email")
        if not user.check_password(password):
            raise AuthenticationFailed("failed pass")

        # token
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        response = Response()

        # set cookies
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}

        return response


class UserAPI(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("unauthenticated")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("unauthenticated")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutAPI(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response